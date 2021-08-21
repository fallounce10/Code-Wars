def domain_name(url):
	if "//" in url:
		if "www" in url:
			return url.split("/")[2].split(".")[1]
		return url.split("/")[2].split(".")[0]
	else:
		return url.split(".")[1]
