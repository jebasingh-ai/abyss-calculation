# 🐳 Abyss Calculation - Docker Edition
# The Most Containerized 1+1 Calculator in the Multiverse

# Stage 1: Universe Builder
FROM ubuntu:latest AS universe-builder

# Install ALL the compilers and interpreters
RUN apt-get update && apt-get install -y \
    # Normal languages
    python3 python3-pip nodejs npm golang-go rustc cargo \
    gcc g++ gfortran openjdk-17-jdk php perl ruby \
    scala dart elixir haskell-platform lua5.3 \
    # Esoteric languages  
    brainfuck befunge intercal lolcode \
    # Domain-specific
    r-base gnat cobc \
    # Build tools
    wget git make automake \
    && rm -rf /var/lib/apt/lists/*

# Install TypeScript and other package managers
RUN npm install -g typescript ts-node

# Install Rockstar interpreter
RUN wget -O /usr/local/bin/rockstar https://github.com/yyyyyyyan/rockstar-py/raw/main/rockstar && \
    chmod +x /usr/local/bin/rockstar

WORKDIR /abyss
COPY . .

# Build all languages
RUN chmod +x build_all_abyss.sh
RUN ./build_all_abyss.sh

# Stage 2: Minimal Runtime
FROM ubuntu:latest AS abyss-runtime

# Only install runtime dependencies
RUN apt-get update && apt-get install -y \
    python3 nodejs default-jre php perl ruby lua5.3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /abyss

# Copy only built artifacts
COPY --from=universe-builder /abyss/dist/ ./dist/
COPY --from=universe-builder /abyss/src/python/ ./src/python/
COPY --from=universe-builder /abyss/src/javascript/ ./src/javascript/
# ... copy other built languages

# Copy the main entry point
COPY --from=universe-builder /abyss/abyss_launcher.sh .

# Cosmic environment variables
ENV ABYSS_LEVEL="MAXIMUM"
ENV QUANTUM_FLUCTUATIONS="ENABLED"
ENV COSMIC_INFLATION="ACTIVE"

# Expose the void
EXPOSE 8080

# Entry point to the abyss
CMD ["./abyss_launcher.sh"]

# Health check - because even the abyss needs to be healthy
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "from src.python.abyss import quick_calculation; print(quick_calculation())" || exit 1

# Labels for cosmic discovery
LABEL org.abyss.calculation.version="2.0.0"
LABEL org.abyss.calculation.license="WTFPL"
LABEL org.abyss.calculation.languages="27+"
LABEL org.abyss.calculation.purpose="Over-engineering 1+1"
