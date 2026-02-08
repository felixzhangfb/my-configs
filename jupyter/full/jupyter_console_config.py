c = get_config()  # type: ignore

#------------------------------------------------------------------------------
# ConnectionFileMixin(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.ConnectionFileMixin.connection_file = ''
# c.ConnectionFileMixin.control_port = 0
# c.ConnectionFileMixin.hb_port = 0
# c.ConnectionFileMixin.iopub_port = 0
# c.ConnectionFileMixin.ip = ''
# c.ConnectionFileMixin.shell_port = 0
# c.ConnectionFileMixin.stdin_port = 0
# c.ConnectionFileMixin.transport = 'tcp'

#------------------------------------------------------------------------------
# JupyterConsoleApp(ConnectionFileMixin) configuration
#------------------------------------------------------------------------------
# c.JupyterConsoleApp.confirm_exit = True
# c.JupyterConsoleApp.connection_file = ''
# c.JupyterConsoleApp.control_port = 0
# c.JupyterConsoleApp.existing = ''
# c.JupyterConsoleApp.hb_port = 0
# c.JupyterConsoleApp.iopub_port = 0
# c.JupyterConsoleApp.ip = ''
# c.JupyterConsoleApp.kernel_manager_class = 'jupyter_client.manager.KernelManager'
# c.JupyterConsoleApp.kernel_name = 'python'
# c.JupyterConsoleApp.shell_port = 0
# c.JupyterConsoleApp.sshkey = ''
# c.JupyterConsoleApp.sshserver = ''
# c.JupyterConsoleApp.stdin_port = 0
# c.JupyterConsoleApp.transport = 'tcp'

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_level = 30
# c.Application.logging_config = {}
# c.Application.show_config = False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------
# c.JupyterApp.answer_yes = False
# c.JupyterApp.config_file = ''
# c.JupyterApp.config_file_name = ''
# c.JupyterApp.generate_config = False
# c.JupyterApp.log_datefmt = '%Y-%m-%d %H:%M:%S'
# c.JupyterApp.log_format = '[%(name)s]%(highlevel)s %(message)s'
# c.JupyterApp.log_level = 30
# c.JupyterApp.logging_config = {}
# c.JupyterApp.show_config = False
# c.JupyterApp.show_config_json = False

#------------------------------------------------------------------------------
# ZMQTerminalIPythonApp(JupyterApp, JupyterConsoleApp) configuration
#------------------------------------------------------------------------------
# c.ZMQTerminalIPythonApp.answer_yes = False
# c.ZMQTerminalIPythonApp.config_file = ''
# c.ZMQTerminalIPythonApp.config_file_name = ''
# c.ZMQTerminalIPythonApp.confirm_exit = True
# c.ZMQTerminalIPythonApp.connection_file = ''
# c.ZMQTerminalIPythonApp.control_port = 0
# c.ZMQTerminalIPythonApp.existing = ''
# c.ZMQTerminalIPythonApp.generate_config = False
# c.ZMQTerminalIPythonApp.hb_port = 0
# c.ZMQTerminalIPythonApp.iopub_port = 0
# c.ZMQTerminalIPythonApp.ip = ''
# c.ZMQTerminalIPythonApp.kernel_manager_class = 'jupyter_client.manager.KernelManager'
# c.ZMQTerminalIPythonApp.kernel_name = 'python'
# c.ZMQTerminalIPythonApp.log_datefmt = '%Y-%m-%d %H:%M:%S'
# c.ZMQTerminalIPythonApp.log_format = '[%(name)s]%(highlevel)s %(message)s'
# c.ZMQTerminalIPythonApp.log_level = 30
# c.ZMQTerminalIPythonApp.logging_config = {}
# c.ZMQTerminalIPythonApp.shell_port = 0
# c.ZMQTerminalIPythonApp.show_config = False
# c.ZMQTerminalIPythonApp.show_config_json = False
# c.ZMQTerminalIPythonApp.sshkey = ''
# c.ZMQTerminalIPythonApp.sshserver = ''
# c.ZMQTerminalIPythonApp.stdin_port = 0
# c.ZMQTerminalIPythonApp.transport = 'tcp'

#------------------------------------------------------------------------------
# ZMQTerminalInteractiveShell(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
# c.ZMQTerminalInteractiveShell.banner = 'Jupyter console {version}\n\n{kernel_banner}'
# c.ZMQTerminalInteractiveShell.callable_image_handler = None
# c.ZMQTerminalInteractiveShell.display_completions = 'multicolumn'
# c.ZMQTerminalInteractiveShell.editing_mode = 'emacs'
# c.ZMQTerminalInteractiveShell.highlight_matching_brackets = True
# c.ZMQTerminalInteractiveShell.highlighting_style = ''
# c.ZMQTerminalInteractiveShell.highlighting_style_overrides = {}
# c.ZMQTerminalInteractiveShell.history_load_length = 1000
# c.ZMQTerminalInteractiveShell.image_handler = 'PIL'
# c.ZMQTerminalInteractiveShell.include_other_output = False
# c.ZMQTerminalInteractiveShell.kernel_is_complete_timeout = 1
# c.ZMQTerminalInteractiveShell.kernel_timeout = 60
# c.ZMQTerminalInteractiveShell.mime_preference = ['image/png', 'image/jpeg', 'image/svg+xml']
# c.ZMQTerminalInteractiveShell.other_output_prefix = 'Remote '
# c.ZMQTerminalInteractiveShell.prompt_includes_vi_mode = True
# c.ZMQTerminalInteractiveShell.simple_prompt = False
# c.ZMQTerminalInteractiveShell.stream_image_handler = []
# c.ZMQTerminalInteractiveShell.tempfile_image_handler = []
# c.ZMQTerminalInteractiveShell.true_color = False
# c.ZMQTerminalInteractiveShell.use_kernel_is_complete = True

#------------------------------------------------------------------------------
# KernelManager(ConnectionFileMixin) configuration
#------------------------------------------------------------------------------
# c.KernelManager.autorestart = True
# c.KernelManager.cache_ports = False
# c.KernelManager.client_class = 'jupyter_client.blocking.BlockingKernelClient'
# c.KernelManager.client_factory = 'jupyter_client.client.KernelClient'
# c.KernelManager.connection_file = ''
# c.KernelManager.control_port = 0
# c.KernelManager.hb_port = 0
# c.KernelManager.iopub_port = 0
# c.KernelManager.ip = ''
# c.KernelManager.shell_port = 0
# c.KernelManager.shutdown_wait_time = 5.0
# c.KernelManager.stdin_port = 0
# c.KernelManager.transport = 'tcp'

#------------------------------------------------------------------------------
# KernelRestarter(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.KernelRestarter.debug = False
# c.KernelRestarter.random_ports_until_alive = True
# c.KernelRestarter.restart_limit = 5
# c.KernelRestarter.stable_start_time = 10.0
# c.KernelRestarter.time_to_dead = 3.0

#------------------------------------------------------------------------------
# Session(Configurable) configuration
#------------------------------------------------------------------------------
# c.Session.buffer_threshold = 1024
# c.Session.check_pid = True
# c.Session.copy_threshold = 65536
# c.Session.debug = False
# c.Session.digest_history_size = 65536
# c.Session.item_threshold = 64
# c.Session.key = b''
# c.Session.keyfile = ''
# c.Session.metadata = {}
# c.Session.packer = 'orjson'
# c.Session.session = ''
# c.Session.signature_scheme = 'hmac-sha256'
# c.Session.unpacker = 'orjson'
# c.Session.username = 'zfb'