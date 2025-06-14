#!/usr/bin/python3
import cmd
import os


class Filemanager(cmd.Cmd):
    prompt = "(fm) "
    intro = "welcome to the filemanager CLI. type help or ? to list command.\n" 

    def emptyline(self):
        """a method that handle empty line passing"""
        return super().emptyline()

    def do_exit(self,arg):
        """exit the file manager CLI"""
        print ("exiting filemanger. goodbye")

    def do_quit (self,line):
        """Quit the file manager"""
        return true

    def do_EOF(sef,line):
        """handle EOF(CTRL + D) to exit the CLI"""
        print ("exiting filemanager.goodbye")
        return true

if __name__ == "__main__":
    Filemanager().cmdloop()