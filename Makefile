EXT_NAME:=com.github.choko256.ulauncher-gen
EXT_DIR:=$(shell pwd)

dev:
	ulauncher --no-extensions --dev v |& grep "gen"
