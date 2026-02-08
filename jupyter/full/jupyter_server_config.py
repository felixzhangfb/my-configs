c = get_config()  # type: ignore

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
# ServerApp(JupyterApp) configuration
#------------------------------------------------------------------------------
# c.ServerApp.allow_credentials = False
# c.ServerApp.allow_external_kernels = False
# c.ServerApp.allow_origin = ''
# c.ServerApp.allow_origin_pat = ''
# c.ServerApp.allow_password_change = True
# c.ServerApp.allow_remote_access = False
# c.ServerApp.allow_root = False
# c.ServerApp.allow_unauthenticated_access = True
# c.ServerApp.answer_yes = False
# c.ServerApp.authenticate_prometheus = True
# c.ServerApp.authorizer_class = 'jupyter_server.auth.authorizer.AllowAllAuthorizer'
# c.ServerApp.autoreload = False
# c.ServerApp.base_url = '/'
# c.ServerApp.browser = ''
# c.ServerApp.certfile = ''
# c.ServerApp.client_ca = ''
# c.ServerApp.config_file = ''
# c.ServerApp.config_file_name = ''
# c.ServerApp.config_manager_class = 'jupyter_server.services.config.manager.ConfigManager'
# c.ServerApp.contents_manager_class = 'jupyter_server.services.contents.largefilemanager.AsyncLargeFileManager'
# c.ServerApp.cookie_options = {}
# c.ServerApp.cookie_secret = b''
# c.ServerApp.cookie_secret_file = ''
# c.ServerApp.custom_display_url = ''
# c.ServerApp.default_url = '/'
# c.ServerApp.disable_check_xsrf = False
# c.ServerApp.external_connection_dir = None
# c.ServerApp.extra_log_scrub_param_keys = []
# c.ServerApp.extra_services = []
# c.ServerApp.extra_static_paths = []
# c.ServerApp.extra_template_paths = []
# c.ServerApp.file_to_run = ''
# c.ServerApp.file_url_prefix = 'notebooks'
# c.ServerApp.generate_config = False
# c.ServerApp.get_secure_cookie_kwargs = {}
# c.ServerApp.identity_provider_class = 'jupyter_server.auth.identity.PasswordIdentityProvider'
# c.ServerApp.iopub_data_rate_limit = 0.0
# c.ServerApp.iopub_msg_rate_limit = 0.0
# c.ServerApp.ip = 'localhost'
# c.ServerApp.jinja_environment_options = {}
# c.ServerApp.jinja_template_vars = {}
# c.ServerApp.jpserver_extensions = {}
# c.ServerApp.kernel_manager_class = 'jupyter_server.services.kernels.kernelmanager.MappingKernelManager'
# c.ServerApp.kernel_spec_manager_class = 'builtins.object'
# c.ServerApp.kernel_websocket_connection_class = 'jupyter_server.services.kernels.connection.base.BaseKernelWebsocketConnection'
# c.ServerApp.kernel_ws_protocol = ''
# c.ServerApp.keyfile = ''
# c.ServerApp.limit_rate = False
# c.ServerApp.local_hostnames = ['localhost']
# c.ServerApp.log_datefmt = '%Y-%m-%d %H:%M:%S'
# c.ServerApp.log_format = '[%(name)s]%(highlevel)s %(message)s'
# c.ServerApp.log_level = 30
# c.ServerApp.logging_config = {}
# c.ServerApp.login_handler_class = 'jupyter_server.auth.login.LegacyLoginHandler'
# c.ServerApp.logout_handler_class = 'jupyter_server.auth.logout.LogoutHandler'
# c.ServerApp.max_body_size = 536870912
# c.ServerApp.max_buffer_size = 536870912
# c.ServerApp.min_open_files_limit = 0
# c.ServerApp.notebook_dir = ''
# c.ServerApp.open_browser = False
# c.ServerApp.password = ''
# c.ServerApp.password_required = False
# c.ServerApp.port = 0
# c.ServerApp.port_retries = 50
# c.ServerApp.preferred_dir = ''
# c.ServerApp.pylab = 'disabled'
# c.ServerApp.quit_button = True
# c.ServerApp.rate_limit_window = 0.0
# c.ServerApp.reraise_server_extension_failures = False
# c.ServerApp.root_dir = ''
# c.ServerApp.session_manager_class = 'builtins.object'
# c.ServerApp.show_config = False
# c.ServerApp.show_config_json = False
# c.ServerApp.shutdown_no_activity_timeout = 0
# c.ServerApp.sock = ''
# c.ServerApp.sock_mode = '0600'
# c.ServerApp.ssl_options = {}
# c.ServerApp.static_immutable_cache = []
# c.ServerApp.terminado_settings = {}
# c.ServerApp.terminals_enabled = False
# c.ServerApp.token = '<DEPRECATED>'
# c.ServerApp.tornado_settings = {}
# c.ServerApp.trust_xheaders = False
# c.ServerApp.use_redirect_file = True
# c.ServerApp.webbrowser_open_new = 2
# c.ServerApp.websocket_compression_options = None
# c.ServerApp.websocket_ping_interval = 0
# c.ServerApp.websocket_ping_timeout = 0
# c.ServerApp.websocket_url = ''

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

#------------------------------------------------------------------------------
# MultiKernelManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.MultiKernelManager.default_kernel_name = 'python3'
# c.MultiKernelManager.kernel_manager_class = 'jupyter_client.ioloop.IOLoopKernelManager'
# c.MultiKernelManager.shared_context = True

#------------------------------------------------------------------------------
# MappingKernelManager(MultiKernelManager) configuration
#------------------------------------------------------------------------------
# c.MappingKernelManager.allow_tracebacks = True
# c.MappingKernelManager.allowed_message_types = []
# c.MappingKernelManager.buffer_offline_messages = True
# c.MappingKernelManager.cull_busy = False
# c.MappingKernelManager.cull_connected = False
# c.MappingKernelManager.cull_idle_timeout = 0
# c.MappingKernelManager.cull_interval = 300
# c.MappingKernelManager.default_kernel_name = 'python3'
# c.MappingKernelManager.kernel_info_timeout = 60
# c.MappingKernelManager.kernel_manager_class = 'jupyter_client.ioloop.IOLoopKernelManager'
# c.MappingKernelManager.root_dir = ''
# c.MappingKernelManager.shared_context = True
# c.MappingKernelManager.traceback_replacement_message = 'An exception occurred at runtime, which is not shown due to security reasons.'
# c.MappingKernelManager.untracked_message_types = ['comm_info_request', 'comm_info_reply', 'kernel_info_request', 'kernel_info_reply', 'shutdown_request', 'shutdown_reply', 'interrupt_request', 'interrupt_reply', 'debug_request', 'debug_reply', 'stream', 'display_data', 'update_display_data', 'execute_input', 'execute_result', 'error', 'status', 'clear_output', 'debug_event', 'input_request', 'input_reply']

#------------------------------------------------------------------------------
# KernelSpecManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.KernelSpecManager.allowed_kernelspecs = set()
# c.KernelSpecManager.ensure_native_kernel = True
# c.KernelSpecManager.kernel_spec_class = 'jupyter_client.kernelspec.KernelSpec'
# c.KernelSpecManager.whitelist = set()

#------------------------------------------------------------------------------
# AsyncMultiKernelManager(MultiKernelManager) configuration
#------------------------------------------------------------------------------
# c.AsyncMultiKernelManager.default_kernel_name = 'python3'
# c.AsyncMultiKernelManager.kernel_manager_class = 'jupyter_client.ioloop.AsyncIOLoopKernelManager'
# c.AsyncMultiKernelManager.shared_context = True
# c.AsyncMultiKernelManager.use_pending_kernels = False

#------------------------------------------------------------------------------
# AsyncMappingKernelManager(MappingKernelManager, AsyncMultiKernelManager) configuration
#------------------------------------------------------------------------------
# c.AsyncMappingKernelManager.allow_tracebacks = True
# c.AsyncMappingKernelManager.allowed_message_types = []
# c.AsyncMappingKernelManager.buffer_offline_messages = True
# c.AsyncMappingKernelManager.cull_busy = False
# c.AsyncMappingKernelManager.cull_connected = False
# c.AsyncMappingKernelManager.cull_idle_timeout = 0
# c.AsyncMappingKernelManager.cull_interval = 300
# c.AsyncMappingKernelManager.default_kernel_name = 'python3'
# c.AsyncMappingKernelManager.kernel_info_timeout = 60
# c.AsyncMappingKernelManager.kernel_manager_class = 'jupyter_client.ioloop.AsyncIOLoopKernelManager'
# c.AsyncMappingKernelManager.root_dir = ''
# c.AsyncMappingKernelManager.shared_context = True
# c.AsyncMappingKernelManager.traceback_replacement_message = 'An exception occurred at runtime, which is not shown due to security reasons.'
# c.AsyncMappingKernelManager.untracked_message_types = ['comm_info_request', 'comm_info_reply', 'kernel_info_request', 'kernel_info_reply', 'shutdown_request', 'shutdown_reply', 'interrupt_request', 'interrupt_reply', 'debug_request', 'debug_reply', 'stream', 'display_data', 'update_display_data', 'execute_input', 'execute_result', 'error', 'status', 'clear_output', 'debug_event', 'input_request', 'input_reply']
# c.AsyncMappingKernelManager.use_pending_kernels = False

#------------------------------------------------------------------------------
# ContentsManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.ContentsManager.allow_hidden = False
# c.ContentsManager.checkpoints = None
# c.ContentsManager.checkpoints_class = 'jupyter_server.services.contents.checkpoints.Checkpoints'
# c.ContentsManager.checkpoints_kwargs = {}
# c.ContentsManager.event_logger = None
# c.ContentsManager.files_handler_class = 'jupyter_server.files.handlers.FilesHandler'
# c.ContentsManager.files_handler_params = {}
# c.ContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*~']
# c.ContentsManager.post_save_hook = None
# c.ContentsManager.pre_save_hook = None
# c.ContentsManager.preferred_dir = ''
# c.ContentsManager.root_dir = '/'
# c.ContentsManager.untitled_directory = 'Untitled Folder'
# c.ContentsManager.untitled_file = 'untitled'
# c.ContentsManager.untitled_notebook = 'Untitled'

#------------------------------------------------------------------------------
# FileManagerMixin(LoggingConfigurable, Configurable) configuration
#------------------------------------------------------------------------------
# c.FileManagerMixin.hash_algorithm = 'sha256'
# c.FileManagerMixin.use_atomic_writing = True

#------------------------------------------------------------------------------
# FileContentsManager(FileManagerMixin, ContentsManager) configuration
#------------------------------------------------------------------------------
# c.FileContentsManager.allow_hidden = False
# c.FileContentsManager.always_delete_dir = False
# c.FileContentsManager.checkpoints = None
# c.FileContentsManager.checkpoints_class = 'jupyter_server.services.contents.checkpoints.Checkpoints'
# c.FileContentsManager.checkpoints_kwargs = {}
# c.FileContentsManager.delete_to_trash = True
# c.FileContentsManager.event_logger = None
# c.FileContentsManager.files_handler_class = 'jupyter_server.files.handlers.FilesHandler'
# c.FileContentsManager.files_handler_params = {}
# c.FileContentsManager.hash_algorithm = 'sha256'
# c.FileContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*~']
# c.FileContentsManager.max_copy_folder_size_mb = 500
# c.FileContentsManager.post_save_hook = None
# c.FileContentsManager.pre_save_hook = None
# c.FileContentsManager.preferred_dir = ''
# c.FileContentsManager.root_dir = ''
# c.FileContentsManager.untitled_directory = 'Untitled Folder'
# c.FileContentsManager.untitled_file = 'untitled'
# c.FileContentsManager.untitled_notebook = 'Untitled'
# c.FileContentsManager.use_atomic_writing = True

#------------------------------------------------------------------------------
# AsyncContentsManager(ContentsManager) configuration
#------------------------------------------------------------------------------
# c.AsyncContentsManager.allow_hidden = False
# c.AsyncContentsManager.checkpoints = None
# c.AsyncContentsManager.checkpoints_class = 'jupyter_server.services.contents.checkpoints.AsyncCheckpoints'
# c.AsyncContentsManager.checkpoints_kwargs = {}
# c.AsyncContentsManager.event_logger = None
# c.AsyncContentsManager.files_handler_class = 'jupyter_server.files.handlers.FilesHandler'
# c.AsyncContentsManager.files_handler_params = {}
# c.AsyncContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*~']
# c.AsyncContentsManager.post_save_hook = None
# c.AsyncContentsManager.pre_save_hook = None
# c.AsyncContentsManager.preferred_dir = ''
# c.AsyncContentsManager.root_dir = '/'
# c.AsyncContentsManager.untitled_directory = 'Untitled Folder'
# c.AsyncContentsManager.untitled_file = 'untitled'
# c.AsyncContentsManager.untitled_notebook = 'Untitled'

#------------------------------------------------------------------------------
# AsyncFileManagerMixin(FileManagerMixin) configuration
#------------------------------------------------------------------------------
# c.AsyncFileManagerMixin.hash_algorithm = 'sha256'
# c.AsyncFileManagerMixin.use_atomic_writing = True

#------------------------------------------------------------------------------
# AsyncFileContentsManager(FileContentsManager, AsyncFileManagerMixin, AsyncContentsManager) configuration
#------------------------------------------------------------------------------
# c.AsyncFileContentsManager.allow_hidden = False
# c.AsyncFileContentsManager.always_delete_dir = False
# c.AsyncFileContentsManager.checkpoints = None
# c.AsyncFileContentsManager.checkpoints_class = 'jupyter_server.services.contents.checkpoints.AsyncCheckpoints'
# c.AsyncFileContentsManager.checkpoints_kwargs = {}
# c.AsyncFileContentsManager.delete_to_trash = True
# c.AsyncFileContentsManager.event_logger = None
# c.AsyncFileContentsManager.files_handler_class = 'jupyter_server.files.handlers.FilesHandler'
# c.AsyncFileContentsManager.files_handler_params = {}
# c.AsyncFileContentsManager.hash_algorithm = 'sha256'
# c.AsyncFileContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store', '*~']
# c.AsyncFileContentsManager.max_copy_folder_size_mb = 500
# c.AsyncFileContentsManager.post_save_hook = None
# c.AsyncFileContentsManager.pre_save_hook = None
# c.AsyncFileContentsManager.preferred_dir = ''
# c.AsyncFileContentsManager.root_dir = ''
# c.AsyncFileContentsManager.untitled_directory = 'Untitled Folder'
# c.AsyncFileContentsManager.untitled_file = 'untitled'
# c.AsyncFileContentsManager.untitled_notebook = 'Untitled'
# c.AsyncFileContentsManager.use_atomic_writing = True

#------------------------------------------------------------------------------
# NotebookNotary(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.NotebookNotary.algorithm = 'sha256'
# c.NotebookNotary.data_dir = ''
# c.NotebookNotary.db_file = ''
# c.NotebookNotary.secret = b''
# c.NotebookNotary.secret_file = ''
# c.NotebookNotary.store_factory = traitlets.Undefined

#------------------------------------------------------------------------------
# GatewayMappingKernelManager(AsyncMappingKernelManager) configuration
#------------------------------------------------------------------------------
# c.GatewayMappingKernelManager.allow_tracebacks = True
# c.GatewayMappingKernelManager.allowed_message_types = []
# c.GatewayMappingKernelManager.buffer_offline_messages = True
# c.GatewayMappingKernelManager.cull_busy = False
# c.GatewayMappingKernelManager.cull_connected = False
# c.GatewayMappingKernelManager.cull_idle_timeout = 0
# c.GatewayMappingKernelManager.cull_interval = 300
# c.GatewayMappingKernelManager.default_kernel_name = 'python3'
# c.GatewayMappingKernelManager.kernel_info_timeout = 60
# c.GatewayMappingKernelManager.kernel_manager_class = 'jupyter_client.ioloop.AsyncIOLoopKernelManager'
# c.GatewayMappingKernelManager.root_dir = ''
# c.GatewayMappingKernelManager.shared_context = True
# c.GatewayMappingKernelManager.traceback_replacement_message = 'An exception occurred at runtime, which is not shown due to security reasons.'
# c.GatewayMappingKernelManager.untracked_message_types = ['comm_info_request', 'comm_info_reply', 'kernel_info_request', 'kernel_info_reply', 'shutdown_request', 'shutdown_reply', 'interrupt_request', 'interrupt_reply', 'debug_request', 'debug_reply', 'stream', 'display_data', 'update_display_data', 'execute_input', 'execute_result', 'error', 'status', 'clear_output', 'debug_event', 'input_request', 'input_reply']
# c.GatewayMappingKernelManager.use_pending_kernels = False

#------------------------------------------------------------------------------
# GatewayKernelSpecManager(KernelSpecManager) configuration
#------------------------------------------------------------------------------
# c.GatewayKernelSpecManager.allowed_kernelspecs = set()
# c.GatewayKernelSpecManager.ensure_native_kernel = True
# c.GatewayKernelSpecManager.kernel_spec_class = 'jupyter_client.kernelspec.KernelSpec'
# c.GatewayKernelSpecManager.whitelist = set()

#------------------------------------------------------------------------------
# SessionManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.SessionManager.database_filepath = ':memory:'

#------------------------------------------------------------------------------
# GatewaySessionManager(SessionManager) configuration
#------------------------------------------------------------------------------
# c.GatewaySessionManager.database_filepath = ':memory:'

#------------------------------------------------------------------------------
# BaseKernelWebsocketConnection(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.BaseKernelWebsocketConnection.kernel_ws_protocol = None
# c.BaseKernelWebsocketConnection.session = None

#------------------------------------------------------------------------------
# GatewayWebSocketConnection(BaseKernelWebsocketConnection) configuration
#------------------------------------------------------------------------------
# c.GatewayWebSocketConnection.kernel_ws_protocol = ''
# c.GatewayWebSocketConnection.session = None

#------------------------------------------------------------------------------
# GatewayClient(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
# c.GatewayClient.accept_cookies = False
# c.GatewayClient.allowed_envs = ''
# c.GatewayClient.auth_header_key = ''
# c.GatewayClient.auth_scheme = ''
# c.GatewayClient.auth_token = None
# c.GatewayClient.ca_certs = None
# c.GatewayClient.client_cert = None
# c.GatewayClient.client_key = None
# c.GatewayClient.connect_timeout = 40.0
# c.GatewayClient.env_whitelist = ''
# c.GatewayClient.event_logger = None
# c.GatewayClient.gateway_retry_interval = 1.0
# c.GatewayClient.gateway_retry_interval_max = 30.0
# c.GatewayClient.gateway_retry_max = 5
# c.GatewayClient.gateway_token_renewer_class = 'jupyter_server.gateway.gateway_client.GatewayTokenRenewerBase'
# c.GatewayClient.headers = '{}'
# c.GatewayClient.http_pwd = None
# c.GatewayClient.http_user = None
# c.GatewayClient.kernels_endpoint = '/api/kernels'
# c.GatewayClient.kernelspecs_endpoint = '/api/kernelspecs'
# c.GatewayClient.kernelspecs_resource_endpoint = '/kernelspecs'
# c.GatewayClient.launch_timeout_pad = 2.0
# c.GatewayClient.request_timeout = 42.0
# c.GatewayClient.url = None
# c.GatewayClient.validate_cert = True
# c.GatewayClient.ws_url = None

#------------------------------------------------------------------------------
# EventLogger(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
# c.EventLogger.handlers = None

#------------------------------------------------------------------------------
# ZMQChannelsWebsocketConnection(BaseKernelWebsocketConnection) configuration
#------------------------------------------------------------------------------
# c.ZMQChannelsWebsocketConnection.iopub_data_rate_limit = 1000000
# c.ZMQChannelsWebsocketConnection.iopub_msg_rate_limit = 1000
# c.ZMQChannelsWebsocketConnection.kernel_ws_protocol = None
# c.ZMQChannelsWebsocketConnection.limit_rate = True
# c.ZMQChannelsWebsocketConnection.rate_limit_window = 3
# c.ZMQChannelsWebsocketConnection.session = None