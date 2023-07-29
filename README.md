
# Bulk images
Download multiple images with certain size randomly or with a query

## Used packages
**Require installation**

[Duckduckgo_search](https://github.com/deedy5/duckduckgo_search) by deedy5

## How to use

 - Install packages and download img_bulk.py
 - To get just a certain amount of pics run:

>   $ python3 img_bulk.py (number of pics)

>   $ python3 img_bulk.py 5
  - To get pics with minimal resolution:
  > $ python3 img_bulk.py (number of pics) (min width)x(min height)

  > $ python3 img_bulk.py 5 1920x1080

 > $ python3 img_bulk.py 5 0x2000
  - To get certain pictures:
  > $ python3 img_bulk.py (number of pics) (query)

  > $ python3 img_bulk.py 5 car sunset
  - Combine both:
  > $ python3 img_bulk.py (number of pics) (min width)x(min height)) (query)

  > $ python3 img_bulk.py 5 2000x0 car sunset

**Output will be in the archive img_bulk.zip**

It rewrites on every execution

## To do
 - Multiple file output

## Similar services
 - [unsample.net](https://unsample.net/)
 - [picsum.photos](https://picsum.photos/)
