from setuptools import setup, find_packages

setup(
    name="ollama-agent",
    version="0.1.0",
    packages=find_packages(),
    py_modules=["agent", "cli", "ollama_client", "schemas", "state", "tools"],
    install_requires=[
        "requests",
        "pydantic",
    ],
    entry_points={
        "console_scripts": [
            "oc=cli:main", # 'oc' 라는 명령어로 실행되도록 설정
        ],
    },
)
