# bash-markdown

preview markdown file in browser

## install

build.sh will build the docker image for web server

```
./build.sh
```

install.sh will install the bash script to /usr/local/bin

```
./install.sh
```

## usage

Change to the directory where the markdown file is located.
Run the command below to start the web server. -p option is optional, default port is 8080.

```
markdown -p 8080
```

Access to [http://localhost:8080/YOUFILE.md](http://localhost:8080/YOUFILE.md)

## debug

Same as install. Run build.sh to build the docker image.

```
./build.sh
```

Run run.sh to start the web server.

```
./run.sh
```

Access to [http://localhost:8080/index.md](http://localhost:8080/index.md)
