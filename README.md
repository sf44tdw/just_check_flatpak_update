# just_check_flatpak_update
flatpakのアップデートチェックをやるだけのコマンド。
("gnome-software"をインストールしている場合はそれで代替できるため、これを利用する必要はない。)

## RPMパッケージのビルドとインストール

RPMのビルドに必要な`rpmbuild`を用意したうえで、リポジトリのルートから実行します。

```sh
rpmbuild --define "_sourcedir $PWD/src" -ba flatpak-update-timer.spec
sudo dnf install "$HOME"/rpmbuild/RPMS/noarch/flatpak-update-timer-1.0-*.noarch.rpm
```

稼働中のsystemd上ではインストール時にtimerを有効化・開始します。削除時にはRPMのsystemdマクロがtimerを停止・無効化します。

```sh
sudo dnf remove flatpak-update-timer
```
