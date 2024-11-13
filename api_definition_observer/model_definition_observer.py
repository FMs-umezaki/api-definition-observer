import ast
import os
import sys
import tempfile

import git
import openpyxl
import yaml


class ModelObserver:
    def observe_model_update(self, file_path: str):
        repo = git.Repo(f"{os.path.dirname(__file__)}/../..")

        # sweets/PRE/GEN4_PROGRAM_UPDATE-MAINの最初のコミットを取得
        commit = repo.commit("627932a930c3a7ee8567612447e13708349cf289")
        print(commit)

        with open(file_path, "r") as f:
            definition = yaml.load(f)
            print(definition)

        exit(1)


def observe_model_update():
    if len(sys.argv) < 2:
        print("[ERROR] 定義のYamlファイルが指定されていません")
        sys.exit(1)

    ModelObserver().observe_model_update(file_path=sys.argv[1])
