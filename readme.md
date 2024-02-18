
# プロジェクトセットアップ手順

このガイドでは、プロジェクト用の仮想環境のセットアップ、必要なパッケージのインストール、そして環境の依存関係を保存する方法について説明します。

## 仮想環境の作成

環境ディレクトリに`onnx`という名前の仮想環境を作成するには、ターミナルまたはコマンドプロンプトで以下のコマンドを実行します：

```bash
python -m venv %USERPROFILE%\envs\onnx && %USERPROFILE%\envs\onnx\Scripts\activate
```

## パッケージのインストール

- `requirements.txt`ファイルからパッケージをインストールするには、以下のコマンドを使用します：

  ```bash
  pip install -r requirements.txt
  ```

- または、インストールバッチファイル（例：`install_onnx.bat`）がある場合は、ダブルクリックするかコマンドラインから直接実行してパッケージをインストールします。

## 仮想環境のパッケージを保存

仮想環境にインストールされたパッケージのリストを保存するには、`export_requirements.py`スクリプトを使用できます。

`export_requirements.py`スクリプトは、アクティベートされた仮想環境内で実行されることを確認してください。これにより、環境の現在の状態が正確にキャプチャされます。

  ```bash
  python export_requirements.py
  ```