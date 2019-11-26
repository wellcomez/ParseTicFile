package main

import (
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
)

func getFileName(s string) (string, error) {
	u, err := url.Parse(s)
	if err != nil {
		return "", err
	}
	sss := strings.Split(u.Path, "/")
	return sss[len(sss)-1], nil
}
func download(url string) {
	res, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	filename, _ := getFileName(url)
	if len(filename) > 0 {
		f, err := os.Create(filename)
		if err != nil {
			panic(err)
		}
		io.Copy(f, res.Body)
	}
}
func main() {

}
