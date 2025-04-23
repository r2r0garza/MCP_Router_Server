from setuptools import setup, find_packages

setup(
    name="mcp_client",
    version="1.0.0",
    description="Python client for MCP Router Server",
    author="MCP Router Server Contributors",
    packages=find_packages(),
    install_requires=["requests"],
    python_requires=">=3.7",
)
