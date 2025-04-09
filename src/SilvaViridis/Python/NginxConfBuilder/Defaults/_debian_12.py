from SilvaViridis.Python.Common.Web import MimeType

from ..Common import (
    OnOff,
    Path,
    Size,
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
    Sendfile,
    TcpNopush,
    TypesHashMaxSize,
)

from ..Modules.HttpGzip import (
    Gzip,
)

from ..Modules.HttpLog import (
    AccessLog,
)

from ..Modules.HttpSsl import (
    SslPreferServerCiphers,
    SslProtocols,
)

def get_debian_12_default_conf(
) -> MainContext:
    return MainContext(
        user = User(
            order = 100,
            user = "www-data",
        ),
        worker_processes = WorkerProcesses(
            order = 200,
            quantity = "auto",
        ),
        pid = Pid(
            order = 300,
            file = Path("/run/nginx.pid"),
        ),
        error_log = ErrorLog(
            order = 400,
            file = Path("/var/log/nginx/error.log"),
            level = None,
        ),
        include_list = [
            Include(
                order = 500,
                file = Path("/etc/nginx/modules-enabled/*.conf"),
            ),
        ],
        events = Events(
            order = 600,
            worker_connections = WorkerConnections(
                order = 100,
                quantity = 768,
            ),
        ),
        http = Http(
            order = 700,
            sendfile = Sendfile(
                order = 100,
                state = OnOff.on,
            ),
            tcp_nopush = TcpNopush(
                order = 200,
                state = OnOff.on,
            ),
            types_hash_max_size = TypesHashMaxSize(
                order = 300,
                size = Size(value = 2048),
            ),
            include_list = [
                Include(
                    order = 400,
                    file = Path("/etc/nginx/mime.types"),
                ),
                Include(
                    order = 1000,
                    file = Path("/etc/nginx/conf.d/*.conf"),
                ),
                Include(
                    order = 1100,
                    file = Path("/etc/nginx/sites-enabled/*"),
                ),
            ],
            default_type = DefaultType(
                order = 500,
                mime_type = MimeType.application__octet_stream,
            ),
            ssl_protocols = SslProtocols(
                order = 600,
                TLSv1 = True,
                TLSv1_1 = True,
                TLSv1_2 = True,
                TLSv1_3 = True,
            ),
            ssl_prefer_server_ciphers = SslPreferServerCiphers(
                order = 700,
                state = OnOff.on,
            ),
            access_log = AccessLog(
                order = 800,
                path = Path("/var/log/nginx/access.log"),
                format = None,
            ),
            gzip = Gzip(
                order = 900,
                state = OnOff.on,
            ),
        ),
    )
