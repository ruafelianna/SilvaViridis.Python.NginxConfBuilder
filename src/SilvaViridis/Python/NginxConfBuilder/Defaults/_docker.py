from SilvaViridis.Python.Common.Web import MimeType

from ..Common import (
    LogLevel,
    OnOff,
    Path,
    TimeInterval,
)

from ..Modules import MainContext

from ..Modules.Core import (
    ErrorLog,
    Events,
    Include,
    Pid,
    User,
    WorkerConnections,
    WorkerProcesses
)

from ..Modules.HttpCore import (
    DefaultType,
    Http,
    KeepaliveTimeout,
    Sendfile,
)

from ..Modules.HttpCore.Variables import (
    VAR_REMOTE_ADDR,
    VAR_REMOTE_USER,
    VAR_TIME_LOCAL,
    VAR_REQUEST,
    VAR_STATUS,
    VAR_BODY_BYTES_SENT,
    HttpVariable,
)

from ..Modules.HttpLog import (
    AccessLog,
    LogFormat,
)

def get_docker_default_conf(
) -> MainContext:
    return MainContext(
        user = User(
            order = 100,
            user = "nginx",
        ),
        worker_processes = WorkerProcesses(
            order = 200,
            quantity = "auto",
        ),
        error_log = ErrorLog(
            order = 300,
            file = Path("/var/log/nginx/error.log"),
            level = LogLevel.notice,
        ),
        pid = Pid(
            order = 400,
            file = Path("/var/run/nginx.pid"),
        ),
        events = Events(
            order = 500,
            worker_connections = WorkerConnections(
                order = 100,
                quantity = 1024,
            ),
        ),
        http = Http(
            order = 600,
            include_list = [
                Include(
                    order = 100,
                    file = Path("/etc/nginx/mime.types"),
                ),
                Include(
                    order = 700,
                    file = Path("/etc/nginx/conf.d/*.conf"),
                ),
            ],
            default_type = DefaultType(
                order = 200,
                mime_type = MimeType.application__octet_stream,
            ),
            log_format = LogFormat(
                order = 300,
                name = "main",
                strings = [
                    f"{VAR_REMOTE_ADDR} - {VAR_REMOTE_USER} [{VAR_TIME_LOCAL}] "
                    + f"\"{VAR_REQUEST}\" {VAR_STATUS} {VAR_BODY_BYTES_SENT} "
                    + f"\"{HttpVariable("referer")}\" \"{HttpVariable("user_agent")}\" \"{HttpVariable("x_forwarded_for")}\"",
                ],
            ),
            access_log = AccessLog(
                order = 400,
                path = Path("/var/log/nginx/access.log"),
                format = "main",
            ),
            sendfile = Sendfile(
                order = 500,
                state = OnOff.on,
            ),
            keepalive_timeout = KeepaliveTimeout(
                order = 600,
                time = TimeInterval(value = 65),
            ),
        ),
    )
