#!/usr/bin/env python
import cmd, sys
from fbl_tables import *

class FBLShell(cmd.Cmd):
      intro = 'Welcome to the FBL shell.   Type help or ? to list commands.\n'
      prompt = '(FBL) '
      file = None
      def do_br_wind(self, arg):
            'What wind'
            print(simple_table("wind","wind_type","d6"))

      def do_br_snowfall(self, arg):
            'What snowfall'
            print(simple_table("snowfall","snowfall_type","d6"))
      def do_br_cold(self, arg):
            'What cold'
            if (arg):
                  incr = int(arg)
            else:
                  incr = 0
            print(simple_table("cold","cold_type","d6", incr))

if __name__ == '__main__':
    FBLShell().cmdloop()
