## 仮想環境の作成

環境ディレクトリに`onnx`という名前の仮想環境を作成するには、ターミナルまたはコマンドプロンプトで以下のコマンドを実行します：

```bash
python -m venv %USERPROFILE%\envs\onnx-cpu_torch && %USERPROFILE%\envs\onnx-cpu_torch\Scripts\activate
```

## パッケージのインストール

- `requirements.txt`ファイルからパッケージをインストールするには、以下のコマンドを使用します：

  ```bash
  pip install -r requirements.txt
  ```

- または、インストールバッチファイル（例：`install_onnx.bat`）がある場合は、ダブルクリックするかコマンドラインから直接実行してパッケージをインストールできる

## 仮想環境のパッケージを保存

仮想環境にインストールされたパッケージのリストを保存するには、`export_requirements.py`スクリプトを使用


  ```bash
  python export_requirements.py
  ```