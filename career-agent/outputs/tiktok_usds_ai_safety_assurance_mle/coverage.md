# TikTok USDS AI Safety & Assurance MLE - Coverage

| Requirement | Coverage | Canonical support | Boundary |
|---|---|---|---|
| Automated LLM/GPAI safety evaluation | Strong adjacent | LLM-as-judge, agent-as-judge, targeted behavioral scenarios, factual consistency and tool calls | Quality/alignment evaluation, not toxicity or prompt-injection defense |
| Continuous monitoring and observability | Strong adjacent | Internal batch evaluation, dashboards, evaluator versioning, model-release reports | Not a real-time centralized observability platform |
| Bias and fairness measurement | Strong | Bayesian demographic-gap risk analysis | Vision-product context, not recommendation-policy enforcement |
| Auditable evaluation | Strong | Reference-based multi-stage evaluator and human validation | Evaluator auditability, not model/data lineage control plane |
| High-throughput evaluation | Partial | Scaled on existing batch infrastructure; debugged throughput/rate limits | Did not build distributed infrastructure |
| Model mitigation and fine-tuning | Adjacent | Targeted vision-model fine-tuning on discovered failure slices | Traditional vision models, not GPAI safety fine-tuning |
| Python/C++ and ML fundamentals | Strong | Production ML evaluation work; Python and C++ | PyTorch not recorded in canonical evidence |
| Distributed systems and Spark/Flink/Kafka | Missing | None | Athena SQL and existing batch platform are not equivalent |
| Recommendation systems | Missing | None | Do not claim |
| Real-time low-latency safety filters | Missing | None | Do not claim |
| RLHF/DPO and prompt-injection defense | Missing | None | Do not claim |
| Regulatory-policy translation | Missing | None | Do not claim |

## Positioning

The strongest case is an evaluation-focused ML engineer who has built auditable model-quality systems, scaled automated judges, measured fairness risk, diagnosed production-model failures, and translated findings into model-development actions. Distributed infrastructure, real-time safeguards, and recommendation systems remain major gaps.
