<!-- Copy w_template folder by every project -->
Duplicate per week: cp -R w_template/ w1/ then rename files.

Update Quarto _quarto.yml to include projects/ or w*/report.qmd in the build.

<!-- Custom additions per week -->
Week 3 (ML): add models/ for saved .pkl/.joblib files.
Week 5 (BI): drop ERD PDFs in output/diagrams/.
Week 6 (end-to-end): you might nest a mini-app or API; put that under src/ or service/.