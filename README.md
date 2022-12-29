# HTTP Web Proxy Server with a blacklist URL filter

In this project, you will learn how web proxy servers work and one of their basic functionalities caching. Your task is to develop a small web proxy server which can cache web pages. It is a very simple proxy server which only understands simple GET-requests, but is able to handle all kinds of objects - not just HTML pages, but
also images.

## Project PDF
[Link To Project PDF](./CSE%20351%20CAS%20Project%20Fall%202022.pdf)


### Note
  Don't forget to add filter.txt file to avoid this error:
   ```
  Traceback (most recent call last):
  File ".../proxyServer.py", line 39, in <module>
    filterdURL = open("filter.txt", "r")
  FileNotFoundError: [Errno 2] No such file or directory: 'filter.txt'
   ```