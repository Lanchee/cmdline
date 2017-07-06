'''
get keyboard injection and return the suitable result for you 
by fuzzyfinding you injection history and some SQL keywords
'''
from prompt_toolkit import prompt 
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
import click
from fuzzyfinder import fuzzyfinder
from pygments.lexers.sql import SqlLexer

SQLKeywords = ['select', 'from','insert', 'update', 'delete', 'drop']

class SQLCompleter(Completer):
	def get_completions(self, document, complete_event):
		word_before_cursor = document.get_word_before_cursor(WORD=True)
		matches = fuzzyfinder(word_before_cursor, SQLKeywords)
		for m in matches:
			yield Completion(m, start_position=-len(word_before_cursor))#匹配成功，则预先显示第一个模糊匹配值


while 1:
	user_input = prompt(u"SQL>", #命令提示符
		history=FileHistory("history.txt"), #历史输入记录文件
		auto_suggest=AutoSuggestFromHistory(), #wenti当前历史输入数据无法添加到页框中，待完善
		completer=SQLCompleter(), 
		lexer=SqlLexer)#wenti当前多字符无法高亮
	click.echo_via_pager(user_input)#输出分页器
	if ( user_input == "exit" ):
		break