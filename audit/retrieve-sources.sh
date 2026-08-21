#!/usr/bin/env bash
# Retrieve the audited sources and record their SHA-256 hashes.
# Run from the repository root:  bash audit/retrieve-sources.sh
# Output: audit/sources/ (files) and audit/SOURCES.sha256 (hashes + versions).
set -euo pipefail

DIR="$(dirname "$0")/sources"
OUT="$(dirname "$0")/SOURCES.sha256"
mkdir -p "$DIR"

echo "# Audited sources retrieved $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$OUT"

# MFOEM (Emotion Ontology) -- OBO PURL resolves to the current release
curl -Lsf http://purl.obolibrary.org/obo/MFOEM.owl -o "$DIR/MFOEM.owl"
grep -o 'owl:versionIRI[^>]*>' "$DIR/MFOEM.owl" | head -1 >> "$OUT" || true
sha256sum "$DIR/MFOEM.owl" >> "$OUT"

# MF (Mental Functioning Ontology)
curl -Lsf http://purl.obolibrary.org/obo/MF.owl -o "$DIR/MF.owl"
grep -o 'owl:versionIRI[^>]*>' "$DIR/MF.owl" | head -1 >> "$OUT" || true
sha256sum "$DIR/MF.owl" >> "$OUT"

# SUMO Merge.kif -- pinned to a commit: record the hash explicitly
SUMO_COMMIT="${SUMO_COMMIT:-master}"
if [ "$SUMO_COMMIT" = "master" ]; then
  SUMO_COMMIT=$(curl -Lsf "https://api.github.com/repos/ontologyportal/sumo/commits/master" | grep -m1 '"sha"' | cut -d'"' -f4)
fi
echo "# SUMO commit: $SUMO_COMMIT" >> "$OUT"
curl -Lsf "https://raw.githubusercontent.com/ontologyportal/sumo/$SUMO_COMMIT/Merge.kif" -o "$DIR/Merge.kif"
sha256sum "$DIR/Merge.kif" >> "$OUT"

# FOSSR BDI ontology v0.5
curl -Lsf "https://w3id.org/fossr/ontology/bdi" -H "Accept: text/turtle" -o "$DIR/fossr-bdi.ttl"
sha256sum "$DIR/fossr-bdi.ttl" >> "$OUT"

echo "Wrote $OUT"
cat "$OUT"
