# calorimeterにおける $\pi^{0}$と $\gamma$についてのCNNによる識別
 Geant4でシミュレーションしてからCNNで識別を行うまでの内容を示す。

## 1.Geant4からの出力されるrootファイルについて
　Geant4のシミュレーションは $\pi^{0}$を打ち込むものと $\gamma$を打ち込むものを分けてシミュレーションを行い、それぞれから`pi0.root`と`gamma.root`というrootファイルが生成される。  
　このrootファイルの中には一つの粒子を打ち込んだ時にEnergy DepositがあったTileのみの情報(何回目のEventであったか、Tileの場所、そのEvent内でのTileに落ちたEnergy Depositの合計など)が`"Tile_Edep"`というTTreeに書き込まれている。  
 　`"Tile_Edep"`の構造は以下の表のようになっている。(なお、Gapは検出層、Absorberは吸収層を示す)  
 
|行|Energy Deposit|Event Number|Gap or Absorber|Layer Number|X Tile Number|Y Tile Number|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $\vdots$|||| $\vdots$|||

## 2.rootファイルからCNNに入力するのに使用する形式への変換
