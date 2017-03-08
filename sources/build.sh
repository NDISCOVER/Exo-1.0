# Run this after fonts have been generated

cd ../fonts

FONTS=$(ls *.ttf)

for font in $FONTS
do 
    echo autohinting $font
    ttfautohint -d $font $font.fix
    rm $font
    mv $font.fix $font
done

echo done
