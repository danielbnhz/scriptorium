# Scriptorium — Project Spec

## Unit of Work
One book = one fetch job. Output is a folder per book.

## Data Shape
- Gutenberg ID
- Title
- Author
- Language
- Raw text content
- Date fetched

## Directory Layout on Server
/texts/
  {gutenberg_id}/
    metadata.json
    content.txt

## Source
Project Gutenberg — https://www.gutenberg.org
Catalog mirror: https://gutenberg.org/cache/epub/feeds/

## Future Sources (maybe)
- Internet Archive
- Perseus Digital Library (Greek/Latin)