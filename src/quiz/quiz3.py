# ========================================================================
# Copyright 2020 Emory University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
from typing import Set, Optional, List

from nltk.corpus.reader import Synset

from nltk.corpus import wordnet as wn


def antonyms(word: str, pos: Optional[str] = None) -> Set[str]:
    pass
    ants = set()
    for syn in wn.synsets(word, pos):
        for lemma in syn.lemmas():
            for ant in lemma.antonyms():
                ants.add(ant.name())
    return ants


def lch_paths(word_0: str, word_1: str) -> List[List[Synset]]:
    pass
    synsets_0 = wn.synsets(word_0)
    synsets_1 = wn.synsets(word_1)
    syn_paths = []
    for synset_0 in synsets_0:
        for synset_1 in synsets_1:
            lch = synset_0.lowest_common_hypernyms(synset_1)
            paths = []

            for hypernym in lch:
                paths.extend(hypernym.hypernym_paths())

            syn_paths.append(paths)
    return syn_paths


if __name__ == '__main__':
    print(antonyms('buy', pos='v'))
    for path in lch_paths('dog', 'cat'):
        print(path)
