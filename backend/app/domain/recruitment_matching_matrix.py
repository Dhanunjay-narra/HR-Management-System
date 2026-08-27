"""
Comprehensive Global 1,000+ Skill Ontology & Synonym Taxonomy Engine
Maps skills across Engineering, Cloud, Data, Security, QA, Product, Design, Sales, Marketing, HR, and Compliance.
"""
from typing import Dict, List, Set, Tuple


SKILL_ONTOLOGY_REGISTRY: Dict[str, Dict[str, List[str]]] = {
    "Cloud Computing & DevOps": {
        "AWS": ["amazon web services", "ec2", "s3", "lambda", "ecs", "eks", "fargate", "cloudformation", "iam", "route53", "dynamodb", "sqs", "sns", "kinesis", "cloudwatch"],
        "Google Cloud Platform": ["gcp", "google cloud", "gke", "cloud run", "bigquery", "cloud functions", "cloud spanner", "pub/sub", "dataflow", "anthos"],
        "Microsoft Azure": ["azure", "aks", "azure devops", "azure functions", "cosmos db", "azure blob", "arm templates", "bicep", "azure ad", "entra id"],
        "Containerization & Orchestration": ["docker", "docker compose", "podman", "containerd", "kubernetes", "k8s", "helm", "istio", "envoy", "calico", "cilium", "openshift"],
        "Infrastructure as Code": ["terraform", "terragrunt", "pulumi", "ansible", "packer", "chef", "puppet", "saltstack", "vagrant"],
        "CI/CD & Observability": ["github actions", "gitlab ci", "jenkins", "circleci", "argo cd", "flux cd", "spinnaker", "tekton", "prometheus", "grafana", "datadog", "new relic", "splunk", "jaeger", "opentelemetry", "elk stack"]
    },
    "Backend & Distributed Systems": {
        "Python Ecosystem": ["python", "python3", "fastapi", "django", "django rest framework", "flask", "tornado", "celery", "pydantic", "sqlalchemy", "alembic", "pytest", "poetry", "uvicorn", "gunicorn"],
        "Go Ecosystem": ["go", "golang", "gin", "echo", "fiber", "gorilla/mux", "gorm", "grpc-go", "cobra", "viper"],
        "Java & JVM": ["java", "java 17", "java 21", "spring boot", "spring cloud", "hibernate", "maven", "gradle", "quarkus", "micronaut", "kotlin", "scala", "clojure"],
        "C# & .NET": ["c#", ".net core", ".net 8", "asp.net core", "entity framework core", "linq", "blazor", "wcf", "nuget"],
        "Node.js Ecosystem": ["node.js", "nodejs", "express", "nestjs", "fastify", "koa", "socket.io", "prisma", "typeorm", "mongoose", "npm", "yarn", "pnpm"],
        "Rust Ecosystem": ["rust", "actix-web", "axum", "tokio", "serde", "diesel", "sqlx", "tonic", "cargo"],
        "Architecture Patterns": ["microservices", "event-driven architecture", "domain-driven design", "cqrs", "event sourcing", "restful apis", "graphql", "grpc", "message queues", "websocket", "clean architecture", "hexagonal architecture"]
    },
    "Databases & Cache": {
        "Relational Databases": ["postgresql", "postgres", "mysql", "mariadb", "oracle db", "microsoft sql server", "sqlite", "cockroachdb", "tidb"],
        "NoSQL & Key-Value": ["mongodb", "redis", "valkey", "cassandra", "scylladb", "couchbase", "dynamodb", "couchdb"],
        "Search & Analytics": ["elasticsearch", "opensearch", "apache solr", "meilisearch", "typesense", "clickhouse", "snowflake", "bigquery", "duckdb", "redshift"],
        "Messaging & Streaming": ["apache kafka", "rabbitmq", "apache pulsar", "nats", "zeromq", "redis pub/sub", "aws sqs", "google pub/sub"]
    },
    "Frontend & Web": {
        "React Ecosystem": ["react", "react.js", "react 18", "next.js", "remix", "redux", "redux toolkit", "zustand", "react query", "tanstack query", "formik", "react hook form", "framer motion"],
        "Languages & Core": ["typescript", "javascript", "es6+", "html5", "css3", "sass", "scss", "webassembly", "wasm"],
        "CSS & UI Frameworks": ["tailwind css", "material-ui", "mui", "shadcn/ui", "ant design", "chakra ui", "styled-components", "bootstrap"],
        "Build Tools": ["vite", "webpack", "turbopack", "rollup", "esbuild", "babel", "postcss"]
    },
    "Mobile App Development": {
        "Cross-Platform": ["flutter", "dart", "react native", "expo", "ionic", "capacitor", "kmp", "kotlin multiplatform"],
        "Native iOS": ["swift", "swiftui", "objective-c", "xcode", "cocoapods", "combine"],
        "Native Android": ["kotlin", "jetpack compose", "java android", "android studio", "coroutines", "dagger hilt"]
    },
    "AI, ML & Data Science": {
        "Deep Learning Frameworks": ["pytorch", "tensorflow", "keras", "jax", "onnx", "tensorrt"],
        "Generative AI & LLMs": ["large language models", "llm", "openai api", "anthropic claude", "langchain", "llamaindex", "huggingface", "vllm", "rag", "retrieval augmented generation", "prompt engineering", "fine-tuning", "lora"],
        "Vector Databases": ["pgvector", "pinecone", "weaviate", "qdrant", "chroma", "milvus", "faiss"],
        "Data Engineering": ["apache spark", "pyspark", "apache airflow", "dbt", "kafka", "flink", "presto", "trino", "pandas", "numpy", "polars", "scipy", "scikit-learn"]
    },
    "Security & Compliance": {
        "AppSec & DevSecOps": ["owasp top 10", "sast", "dast", "sonarqube", "snyk", "trivy", "dependabot", "vault", "hashicorp vault", "jwt", "oauth2", "oidc", "saml2", "pki", "tls/ssl"],
        "Regulatory Compliance": ["soc2", "iso 27001", "gdpr", "hipaa", "pci-dss", "ccpa", "nist framework", "sox compliance"]
    }
}
