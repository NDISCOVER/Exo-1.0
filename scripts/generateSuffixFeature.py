f = CurrentFont()

# Set these values for the feature you want
# It should be based on a suffix, for easy cheap magic
setname = 'SmallCaps'
suffix = '.smcp'

# The rest is automatic; copy-paste the output
base = []                    # Base glyphs that match the suffix
subset = []                  # Glyph names to sort
for glyph in f:
    if suffix in glyph.name:
        base.append(glyph)

for i in base:               # Read the objects in the base set
    subset.append(i.name)    # Put their names as strings into the subset

subset.sort()                # Sort the glyph names

print 'lookup feature' + setname + ' {'
print '  lookupflag 0;'

for g in subset:
    name = f[g].name         # Read glyph as an object again
    if suffix == '.smcp':
        clean = f[g].name.replace(suffix, '')[0].lower() + f[g].name.replace(suffix, '')[1:]
    else:
        clean = f[g].name.replace(suffix, '')
    print '    sub \\' + clean + ' by \\' + name + ';'

print '} feature' + setname + ';'
