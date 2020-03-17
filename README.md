# steal-preview
crawling the preview video link of AVHD101

# prerequirements
1. pip install scrapy
2. pip install hanziconv # convert to Trad Chinese from Simp Chinese
3. scrapy runspider avSpider.py -a name=桥本有菜 --nolog 

# Run as http server (default port 23333)
1. npm install express --save
2. node http.js 
3. httpie host:port/v?a={name}&m=1  // m for accurate mode, no m for fuzzy mode

# contributions
First time to use crawler with python, Hope you gays could make it stonger. Old driver come on!
