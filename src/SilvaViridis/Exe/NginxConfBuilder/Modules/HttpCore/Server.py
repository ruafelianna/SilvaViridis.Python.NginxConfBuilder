from collections.abc import Sequence

from .AbsoluteRedirect import AbsoluteRedirect
from .Aio import Aio
from .AioWrite import AioWrite
from .AuthDelay import AuthDelay
from .ChunkedTransferEncoding import ChunkedTransferEncoding
from .ClientBodyBufferSize import ClientBodyBufferSize
from .ClientBodyInFileOnly import ClientBodyInFileOnly
from .ClientBodyInSingleBuffer import ClientBodyInSingleBuffer
from .ClientBodyTempPath import ClientBodyTempPath
from .ClientBodyTimeout import ClientBodyTimeout
from .ClientHeaderBufferSize import ClientHeaderBufferSize
from .ClientHeaderTimeout import ClientHeaderTimeout
from .ClientMaxBodySize import ClientMaxBodySize
from .ConnectionPoolSize import ConnectionPoolSize
from .DefaultType import DefaultType
from .Directio import Directio
from .DirectioAlignment import DirectioAlignment
from .DisableSymlinks import DisableSymlinks
from .ErrorPage import ErrorPage
from .Etag import Etag
from .IfModifiedSince import IfModifiedSince
from .IgnoreInvalidHeaders import IgnoreInvalidHeaders
from .KeepaliveDisable import KeepaliveDisable
from .KeepaliveMinTimeout import KeepaliveMinTimeout
from .KeepaliveRequests import KeepaliveRequests
from .KeepaliveTime import KeepaliveTime
from .KeepaliveTimeout import KeepaliveTimeout
from .LargeClientHeaderBuffers import LargeClientHeaderBuffers
from .LimitRate import LimitRate
from .LimitRateAfter import LimitRateAfter
from .LingeringClose import LingeringClose
from .LingeringTime import LingeringTime
from .LingeringTimeout import LingeringTimeout
from .Listen import Listen
from .Location import Location
from .LogNotFound import LogNotFound
from .LogSubrequest import LogSubrequest
from .MaxRanges import MaxRanges
from .MergeSlashes import MergeSlashes
from .MsiePadding import MsiePadding
from .MsieRefresh import MsieRefresh
from .OpenFileCache import OpenFileCache
from .OpenFileCacheErrors import OpenFileCacheErrors
from .OpenFileCacheMinUses import OpenFileCacheMinUses
from .OpenFileCacheValid import OpenFileCacheValid
from .OutputBuffers import OutputBuffers
from .PortInRedirect import PortInRedirect
from .PostponeOutput import PostponeOutput
from .ReadAhead import ReadAhead
from .RecursiveErrorPages import RecursiveErrorPages
from .RequestPoolSize import RequestPoolSize
from .ResetTimedoutConnection import ResetTimedoutConnection
from .Resolver import Resolver
from .ResolverTimeout import ResolverTimeout
from .Root import Root
from .Satisfy import Satisfy
from .Sendfile import Sendfile
from .SendfileMaxChunk import SendfileMaxChunk
from .SendLowat import SendLowat
from .SendTimeout import SendTimeout
from .ServerName import ServerName
from .ServerNameInRedirect import ServerNameInRedirect
from .ServerTokens import ServerTokens
from .SubrequestOutputBufferSize import SubrequestOutputBufferSize
from .TcpNodelay import TcpNodelay
from .TcpNopush import TcpNopush
from .TryFiles import TryFiles
from .Types import Types
from .TypesHashBucketSize import TypesHashBucketSize
from .TypesHashMaxSize import TypesHashMaxSize
from .UnderscoresInHeaders import UnderscoresInHeaders

from ..Core import (
    ErrorLog,
    Include,
)

from ...Common import DirectiveBase

from ..HttpGzip import (
    Gzip,
)

from ..HttpLog import (
    AccessLog,
)

from ..HttpSsl import (
    SslPreferServerCiphers,
    SslProtocols,
)

DIR_SERVER = "server"

class Server(DirectiveBase):
    def __init__(
        self,
        order : int,
        absolute_redirect : AbsoluteRedirect | None = None,
        access_log : AccessLog | None = None,
        aio : Aio | None = None,
        aio_write : AioWrite | None = None,
        auth_delay : AuthDelay | None = None,
        chunked_transfer_encoding : ChunkedTransferEncoding | None = None,
        client_body_buffer_size : ClientBodyBufferSize | None = None,
        client_body_in_file_only : ClientBodyInFileOnly | None = None,
        client_body_in_single_buffer : ClientBodyInSingleBuffer | None = None,
        client_body_temp_path : ClientBodyTempPath | None = None,
        client_body_timeout : ClientBodyTimeout | None = None,
        client_header_buffer_size : ClientHeaderBufferSize | None = None,
        client_header_timeout : ClientHeaderTimeout | None = None,
        client_max_body_size : ClientMaxBodySize | None = None,
        connection_pool_size : ConnectionPoolSize | None = None,
        default_type : DefaultType | None = None,
        directio : Directio | None = None,
        directio_alignment : DirectioAlignment | None = None,
        disable_symlinks : DisableSymlinks | None = None,
        error_log : ErrorLog | None = None,
        error_page_list : Sequence[ErrorPage] = [],
        etag : Etag | None = None,
        gzip : Gzip | None = None,
        if_modified_since : IfModifiedSince | None = None,
        include_list : Sequence[Include] = [],
        ignore_invalid_headers : IgnoreInvalidHeaders | None = None,
        keepalive_disable : KeepaliveDisable | None = None,
        keepalive_min_timeout : KeepaliveMinTimeout | None = None,
        keepalive_requests : KeepaliveRequests | None = None,
        keepalive_time : KeepaliveTime | None = None,
        keepalive_timeout : KeepaliveTimeout | None = None,
        large_client_header_buffers : LargeClientHeaderBuffers | None = None,
        limit_rate : LimitRate | None = None,
        limit_rate_after : LimitRateAfter | None = None,
        lingering_close : LingeringClose | None = None,
        lingering_time : LingeringTime | None = None,
        lingering_timeout : LingeringTimeout | None = None,
        listen_list : Sequence[Listen] = [],
        location_list : Sequence[Location] = [],
        log_not_found : LogNotFound | None = None,
        log_subrequest : LogSubrequest | None = None,
        max_ranges : MaxRanges | None = None,
        merge_slashes : MergeSlashes | None = None,
        msie_padding : MsiePadding | None = None,
        msie_refresh : MsieRefresh | None = None,
        open_file_cache : OpenFileCache | None = None,
        open_file_cache_errors : OpenFileCacheErrors | None = None,
        open_file_cache_min_uses : OpenFileCacheMinUses | None = None,
        open_file_cache_valid : OpenFileCacheValid | None = None,
        output_buffers : OutputBuffers | None = None,
        port_in_redirect : PortInRedirect | None = None,
        postpone_output : PostponeOutput | None = None,
        read_ahead : ReadAhead | None = None,
        recursive_error_pages : RecursiveErrorPages | None = None,
        request_pool_size : RequestPoolSize | None = None,
        reset_timedout_connection : ResetTimedoutConnection | None = None,
        resolver : Resolver | None = None,
        resolver_timeout : ResolverTimeout | None = None,
        root : Root | None = None,
        satisfy : Satisfy | None = None,
        send_lowat : SendLowat | None = None,
        send_timeout : SendTimeout | None = None,
        sendfile : Sendfile | None = None,
        sendfile_max_chunk : SendfileMaxChunk | None = None,
        server_name : ServerName | None = None,
        server_name_in_redirect : ServerNameInRedirect | None = None,
        server_tokens : ServerTokens | None = None,
        ssl_prefer_server_ciphers : SslPreferServerCiphers | None = None,
        ssl_protocols : SslProtocols | None = None,
        subrequest_output_buffer_size : SubrequestOutputBufferSize | None = None,
        tcp_nodelay : TcpNodelay | None = None,
        tcp_nopush : TcpNopush | None = None,
        try_files : TryFiles | None = None,
        types : Types | None = None,
        types_hash_bucket_size : TypesHashBucketSize | None = None,
        types_hash_max_size : TypesHashMaxSize | None = None,
        underscores_in_headers : UnderscoresInHeaders | None = None,
    ):
        super().__init__(order, DIR_SERVER)
        self.add_directive(absolute_redirect)
        self.add_directive(access_log)
        self.add_directive(aio)
        self.add_directive(aio_write)
        self.add_directive(auth_delay)
        self.add_directive(chunked_transfer_encoding)
        self.add_directive(client_body_buffer_size)
        self.add_directive(client_body_in_file_only)
        self.add_directive(client_body_in_single_buffer)
        self.add_directive(client_body_temp_path)
        self.add_directive(client_body_timeout)
        self.add_directive(client_header_buffer_size)
        self.add_directive(client_header_timeout)
        self.add_directive(client_max_body_size)
        self.add_directive(connection_pool_size)
        self.add_directive(default_type)
        self.add_directive(directio)
        self.add_directive(directio_alignment)
        self.add_directive(disable_symlinks)
        self.add_directive(error_log)

        for error_page in error_page_list:
            self.add_directive(error_page)

        self.add_directive(etag)
        self.add_directive(gzip)
        self.add_directive(if_modified_since)
        self.add_directive(ignore_invalid_headers)

        for include in include_list:
            self.add_directive(include)

        self.add_directive(keepalive_disable)
        self.add_directive(keepalive_min_timeout)
        self.add_directive(keepalive_requests)
        self.add_directive(keepalive_time)
        self.add_directive(keepalive_timeout)
        self.add_directive(large_client_header_buffers)
        self.add_directive(limit_rate)
        self.add_directive(limit_rate_after)
        self.add_directive(lingering_close)
        self.add_directive(lingering_time)
        self.add_directive(lingering_timeout)

        for listen in listen_list:
            self.add_directive(listen)

        for location in location_list:
            self.add_directive(location)

        self.add_directive(log_not_found)
        self.add_directive(log_subrequest)
        self.add_directive(max_ranges)
        self.add_directive(merge_slashes)
        self.add_directive(msie_padding)
        self.add_directive(msie_refresh)
        self.add_directive(open_file_cache)
        self.add_directive(open_file_cache_errors)
        self.add_directive(open_file_cache_min_uses)
        self.add_directive(open_file_cache_valid)
        self.add_directive(output_buffers)
        self.add_directive(port_in_redirect)
        self.add_directive(postpone_output)
        self.add_directive(read_ahead)
        self.add_directive(recursive_error_pages)
        self.add_directive(request_pool_size)
        self.add_directive(reset_timedout_connection)
        self.add_directive(resolver)
        self.add_directive(resolver_timeout)
        self.add_directive(root)
        self.add_directive(satisfy)
        self.add_directive(send_lowat)
        self.add_directive(send_timeout)
        self.add_directive(sendfile)
        self.add_directive(sendfile_max_chunk)
        self.add_directive(server_name)
        self.add_directive(server_name_in_redirect)
        self.add_directive(server_tokens)
        self.add_directive(ssl_prefer_server_ciphers)
        self.add_directive(ssl_protocols)
        self.add_directive(subrequest_output_buffer_size)
        self.add_directive(tcp_nodelay)
        self.add_directive(tcp_nopush)
        self.add_directive(try_files)
        self.add_directive(types)
        self.add_directive(types_hash_bucket_size)
        self.add_directive(types_hash_max_size)
        self.add_directive(underscores_in_headers)
