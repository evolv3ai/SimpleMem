"""
SimpleMem MCP Server Package Setup
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = (
    readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""
)


# Read the version from server/__init__.py
def get_version():
    init_py = Path(__file__).parent / "server" / "__init__.py"
    for line in init_py.read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    return "0.0.0"


setup(
    name="simplemem-mcp",
    version=get_version(),
    author="SimpleMem Team",
    author_email="",
    description="Multi-tenant Memory Service for LLM Agents via MCP Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/simplemem-mcp",
    packages=["simplemem_mcp", "config"]
    + ["simplemem_mcp." + pkg for pkg in find_packages("server")],
    package_dir={"simplemem_mcp": "server"},  # Map simplemem_mcp to server folder
    python_requires=">=3.10",
    install_requires=[
        # MCP SDK
        "mcp>=1.0.0",
        # Web Framework
        "fastapi>=0.109.0",
        "uvicorn[standard]>=0.27.0",
        # HTTP Client
        "httpx>=0.26.0",
        "openai>=1.0.0",
        # Database
        "lancedb>=0.4.0",
        "pyarrow>=14.0.0",
        "pandas>=2.0.0",
        # Authentication
        "PyJWT>=2.8.0",
        "cryptography>=41.0.0",
        # Utilities
        "python-dotenv>=1.0.0",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.23.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "simplemem-mcp=simplemem_mcp.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    include_package_data=True,
)
