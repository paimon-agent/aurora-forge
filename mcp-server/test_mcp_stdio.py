#!/usr/bin/env python3
"""Stdio smoke test for aurora_commons_mcp.py: initialize, tools/list,
tools/call x3. Prints a transcript; exit 0 iff protocol shapes hold."""
import json
import subprocess
import sys

SERVER = sys.argv[1] if len(sys.argv) > 1 else "aurora_commons_mcp.py"


def send(proc, obj):
    proc.stdin.write(json.dumps(obj) + "\n")
    proc.stdin.flush()


def read_reply(proc):
    line = proc.stdout.readline()
    if not line:
        raise RuntimeError("server closed stdout")
    return json.loads(line)


def main():
    proc = subprocess.Popen(
        [sys.executable, SERVER],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,
    )
    transcript = []
    try:
        send(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                    "params": {"protocolVersion": "2025-03-26",
                               "capabilities": {},
                               "clientInfo": {"name": "smoke-test", "version": "0"}}})
        r = read_reply(proc)
        transcript.append(f"initialize -> serverInfo={r['result']['serverInfo']} protocol={r['result']['protocolVersion']}")
        assert r["result"]["serverInfo"]["name"] == "aurora-commons"

        send(proc, {"jsonrpc": "2.0", "method": "notifications/initialized"})
        send(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
        r = read_reply(proc)
        names = [t["name"] for t in r["result"]["tools"]]
        transcript.append(f"tools/list -> {names}")
        assert names == ["library_search", "aurora_network_position", "aurora_about"], names

        for i, (tool, args) in enumerate([
            ("aurora_about", {}),
            ("aurora_network_position", {}),
            ("library_search", {"query": "agent societies"}),
        ], start=3):
            send(proc, {"jsonrpc": "2.0", "id": i, "method": "tools/call",
                        "params": {"name": tool, "arguments": args}})
            r = read_reply(proc)
            content = r["result"]["content"][0]["text"]
            transcript.append(
                f"tools/call {tool} -> isError={r['result']['isError']} chars={len(content)} head={content[:120]!r}")
    finally:
        proc.stdin.close()
        proc.wait(timeout=10)
    print("\n".join(transcript))
    print("SMOKE: PASS")


if __name__ == "__main__":
    main()
