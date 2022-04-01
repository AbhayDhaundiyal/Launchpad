# Launchpad

This is a web app made using Django, this is a simple rental app that lends people launchpads for a particular time period.

Features :

1. The Pads have two states either Active(ready to be taken) or Inactive(already taken).
2. When the pad is taken the Active state beomes False implying the Inactive state.
3. The Inactive state lasts till the validity expires and the state becomes Active again.

Apis :

1. pads/show/ : Shows all the pads detail
2. pads/show/x/ : Show the detail of the pad with id = x
3. pads/book/x/y/ : Books the pad with id = x for y days.
