render-site:
	-rm -rf docs/*
	quarto render .
	git add docs/*
	git commit -m"new rendering"
	git push origin main
