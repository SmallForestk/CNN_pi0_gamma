# calorimeterにおける $\pi^{0}$と $\gamma$についてのCNNによる識別
 Geant4でシミュレーションしてからCNNで識別を行うまでの内容を示す。

## 1.Geant4からの出力されるrootファイルについて
　Geant4のシミュレーションは $\pi^{0}$を打ち込むものと $\gamma$を打ち込むものを分けてシミュレーションを行い、それぞれから`pi0.root`と`gamma.root`というrootファイルが生成される。  
 
　このrootファイルの中には一つの粒子を打ち込んだ時にEnergy DepositがあったTileのみの情報(何回目のEventであったか、Tileの場所、そのEvent内でのTileに落ちたEnergy Depositの合計など)が`"Tile_Edep"`というTTreeに書き込まれている。  
 
 　`"Tile_Edep"`の構造は以下の表のようになっている。(なお、Gapは検出層、Absorberは吸収層を示す)  
|Energy Deposit|Event Number|Gap or Absorber|Layer Number|X Tile Number|Y Tile Number|
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\vdots$| $\vdots$| $\vdots$| $\vdots$| $\vdots$| $\vdots$|

## 2.TTreeからCNNに入力するのに使用する形式への変換
 　TTreeからCNNに使用する形式へ変換することは`make_image.ipynb`で行っていて、変換するのに`Cnn_tool.make_image.hitmap`という関数を使用している。  
  
 　`Cnn_tool.make_image.hitmap`ではまず、読み込みたい`Event Number`でフィルタをかけて、取り出すという操作をしている。その後、100 $\times$100の0でうめられたnumpy arrayを作成したあとで、TTreeを一行ずつ読んでいって、`LayerNumber`や`X Tile Number`、`Y Tile Number`から`Energy Deposit`をnumpy arrayのどこに足し上げるのかを指定して、`Energy Deposit`を足し上げるということを行っている。(なお、`LayerNumber`や`X Tile Number`、`Y Tile Number`のなかで使用するのは2つで射影する方向に合わせてどの2つを取り出すのか変更する) 
  
  　これらの操作をすべての`Event Number`でおこなうことで、Eventごとに2次元のEnergy Deposit情報を作成する。また、`Cnn_tool.make_image.hitmap`ではオプションとして、`viewpoint`があり、ここに入力する数字を変えることで射影する方向を変えることができる。

## 3.Datasetの分割
　　　2.までで作成したDatasetをCNNに入力する前にラベルと`Event　Number`を紐付けて`sklearn.model_selecrtion.train_test_split`でランダムシードの値を乱数を使って指定しつつ、分割する。また、CNNに入力する画像を1枚の場合と3枚の場合で学習させるため、2通り用意する。

## 4.CNNでの学習
　　　CNNでの学習では学習の最中にtraining dataとvalidation dataでlossと $threshold=0.5$としたときの正解率(Accuracy)を出力するようにしている。また、学習後にはtest dataを使ったときの出力と一緒にtest data、もとの正解ラベル、紐付けられた`Event Number`を保存しておくようにしている。
