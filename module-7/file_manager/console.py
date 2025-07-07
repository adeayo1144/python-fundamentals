#!/usr/bin/python3
import cmd
import os
from create import create


class Filemanager(cmd.Cmd):
    prompt = "(fm) "
    intro = "welcome to the filemanager CLI. type help or ? to list command.\n" 

    def emptyline(self):
        """a method that handle empty line passing"""
        return super().emptyline()

    def do_exit(self,arg):
        """exit the file manager CLI"""
        print ("exiting filemanger. goodbye")

    def precmd(self, line):
        """pre-command processing"""
        if line.endswith(")"):
            command = line. strip(). split('()')[0].strip().split(' ')
            args = line.strip().split('(')[1].strip().split(',')
        else:
            command = line. strip().split( ' ')
            args = []
        if len(command) == 2:
            note = command[1].strip()
            method = command[0].strip()
            if len(args) ==2:
                title = args[0].strip()
                body = args[1].split(")") [0].strip()
                new_line = method + " " + note + " [" + title +  ", "+body
                return str(new_line)
            new_line = method + " " + note
            return str(new_line)
        return line
    
    def do_create(self, line):
        """ Create a file with any name of your choice"""
        try:
            args = line.split("[")
            note = args[0].strip()
            if len(args) == 2:
                title = args[1].split (',')[0].strip()
                body = args[1].split(',')[1].strip()
                body.replace('"', "")
                create(note, title, body)
            elif len(args) == 1:
                create(note)
            else:
                raise Exception("**method not found**")
        except Exception as e:
            print(f"Error: {e}")
            

    def do_copy(self, line):
        """Copy information inside a file"""
        print(line)
        pass

    def do_edit(Self, line):
        """Update the information inside a file"""
        pass

    def do_view(self, line):
        """view the content of a file"""
        pass

    def do_delete(self, line):
        """Delete any file of your choice"""
        pass

    def do_quit (self,line):
        """Quit the file manager"""
        return True

    def do_EOF(sef,line):
        """handle EOF(CTRL + D) to exit the CLI"""
        print ("exiting filemanager.goodbye")
        return True

if __name__ == "__main__":
    Filemanager().cmdloop()