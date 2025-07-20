import subprocess

def test_agent_cli_runs():
    proc = subprocess.Popen(
        ["python", "agent/agent_cli.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    try:
        outs, errs = proc.communicate(input="Fiat\nUno\n2020\nGasolina\nPreto\nManual\n20000\n50000\n", timeout=10)
        assert "Consultando veículos compatíveis" in outs
    except Exception:
        proc.kill()
        assert False
