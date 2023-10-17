from subprocess import Popen, run, PIPE


__all__ = ['run_cmd',
           'run_cmd_Popen_fileno',
           'run_cmd_Popen_PIPE']


def run_cmd(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param cmd_str: 执行的cmd命令
    :return:
    if echo_print == 1:scratch.py
        print('\n执行cmd指令="{}"'.format(cmd_str))
    """
    run(cmd_str, shell=True)


def run_cmd_Popen_fileno(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值，python调试界面输出返回值
    :param cmd_string: cmd命令，如：'adb devices'
    :return:
    """

    #print('运行cmd指令：{}'.format(cmd_string))
    return \
        Popen(cmd_string, shell=True, stdout=None, stderr=None).wait()


def run_cmd_Popen_PIPE(cmd_string):
    """
    执行cmd命令，并得到执行后的返回值,python调试界面不输出返回值
    :param cmd_string: cmd命令，如：'adb devices"'
    :return:
    """

    #print('运行cmd指令：{}'.format(cmd_string))
    return \
        Popen(cmd_string, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE,
              encoding='gbk').communicate()[0]


if __name__ == '__main__':
    s = run_cmd_Popen_PIPE('tasklist')
    print(s)
