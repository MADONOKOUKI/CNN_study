### 研究内容



## 0. 開発環境の構築と実行について



## 1. 依存ミドルウェアのセットアップ (Dockerによる開発環境を構築している場合は以下は不要。)

## 2. 開発環境の準備
```
git clone git@github.com:fchollet/keras.git
```
でkerasのインストール

```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```
.zshrc(.bash_profile)に
```
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
```
を書き込み
```
pyenv install 3.6.0
python3 global 3.6.0
python3 --version
```
で
```
Python 3.6.0 :: Anaconda 4.3.1 (x86_64)
```
が出力されると環境は構成済み


## 3. 開発環境を動かす
** 画像の収集方法
```
python3 download_pic.py [検索したい画像の名前]
```
* 保存ディレクトリを指定して画像を自動保存
* 今回はyahoo!の検索エンジンを使用（googleだとAPIを使用すると可能）

```
python3 curry.py
```

```
python3 make_curry.py
```
* refrigerator_of_foodの中に今冷蔵庫の中に入っている食材の画像を保存しておくとする

* 訓練データを色別に保存
* optimizer`adam`を使用して各種パラメータを設定
* テストデータを使用して判定（精度約73%)
## 4. 動作についての説明


## 5. 参考文献

**推薦システムについて**

* [Matrix Factorization](https://qiita.com/ysekky/items/c81ff24da0390a74fc6c)
* [Tinder API](https://gist.github.com/rtt/10403467)
* [Image ・classification](http://blog.kaggle.com/2017/04/03/dogs-vs-cats-redux-playground-competition-winners-interview-bojan-tunguz/)
* [葉物野菜の見極めについて](https://www.slideshare.net/YujiKawakami3/by-keras)
* [勾配効果法の学習率の影響・活性化関数の影響・ニューラルネットワークの構成の影響](http://sonickun.hatenablog.com/entry/2016/07/11/202005)
* [分類系の全体の話の概要](http://sleeping-micchi.hatenablog.com/entry/2016/09/15/004221)
* [多クラスの分類](http://developer-blog.finc.co.jp/post/137854168027/deeplearning%E3%81%A7%E9%A3%9F%E4%BA%8B%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%AF%E3%83%A9%E3%82%B9%E5%88%86%E9%A1%9E%E5%99%A8%E3%82%92%E4%BD%9C%E6%88%90%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F)
* [各検索エンジンでのスクレイピングについて](https://qiita.com/ysdyt/items/565a0bf3228e12a2c503)
* [スクレイピングのコードについて](http://karaage.hatenadiary.jp/entry/2017/08/23/073000)

**画像認識系参考サイト**

* [CNNの実装についてのまとめ](https://qiita.com/icoxfog417/items/5aa1b3f87bb294f84bac)
* [ssd_kerasによる物体認識の手順](http://ai-coordinator.jp/ssd_keras-ubuntu)

**参考論文・調査**

* [モバイルレシピ推薦システム](https://mm.cs.uec.ac.jp/pub/conf11/120306maruyama_5_ppt.pdf)
* [Food Image recognition by using convolutional neural network](https://arxiv.org/pdf/1612.00983.pdf)


## 備考

**README.mdの確認について**
```
pip install grip
grip -b
```
**Vimの練習サイトについて**
* [vimtutor](https://qiita.com/y-temp4/items/3032d22cb5cc6ae3117a)
