from indeed import extract_indeed_pages
from indeed import extract_indeed_jobs

max_indeed_import = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(max_indeed_import)