# Google DeepMind Agent Quality Research Engineer - Coverage

| Requirement | Coverage | Canonical support | Boundary |
|---|---|---|---|
| Realistic agent environments and task suites | Strong adjacent | Simulated-user agent and targeted scenario generation | Evaluation environments, not production agent product ownership |
| Agentic autoraters calibrated to humans | Strong | Agent-as-judge, expert gold sets, human-in-loop validation, 90% alignment on 40 examples | No external frontier-model leaderboard ownership |
| Long-horizon trajectory diagnostics | Strong | Long multimodal interactions, intent/state metrics, factual consistency and tool-call evaluation | No formal trajectory-reward modeling |
| Root-cause failure analysis | Strong | Visual memory, sycophancy, intent misalignment, embedding-based failure discovery | Do not imply automated harness optimization |
| Scalable evaluation infrastructure | Strong | Existing batch platform scaling, rate-limit/throughput debugging, dashboards, versioning | Existing platform, not infrastructure ownership |
| Dataset creation for model development | Adjacent | Segmentation training dataset delivered to foundation-model team | Not agent trajectories or SFT/RL data |
| Automated verifier generation | Missing | None | Do not claim |
| SFT/RL post-training and reward signals | Missing | None | Do not claim LLM training or post-training |

## Positioning

The closest fit is evaluation research: simulated users, agent-as-judge, human calibration, behavioral metrics, long-interaction diagnostics, tool-use analysis, and feedback into model development. The principal gap is direct ownership of verifier generation and SFT/RL data flywheels.
