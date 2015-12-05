#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl
import unittest
import nose.plugins.attrib
import nose.plugins.skip

from . import util

class OptionConstantsTest(unittest.TestCase):
    # CURLOPT_USERNAME was introduced in libcurl-7.19.1
    @util.min_libcurl(7, 19, 1)
    def test_username(self):
        assert hasattr(pycurl, 'USERNAME')
        assert hasattr(pycurl, 'PASSWORD')
        assert hasattr(pycurl, 'PROXYUSERNAME')
        assert hasattr(pycurl, 'PROXYPASSWORD')
    
    # CURLOPT_DNS_SERVERS was introduced in libcurl-7.24.0
    @util.min_libcurl(7, 24, 0)
    def test_dns_servers(self):
        assert hasattr(pycurl, 'DNS_SERVERS')
        
        # Does not work unless libcurl was built against c-ares
        #c = pycurl.Curl()
        #c.setopt(c.DNS_SERVERS, '1.2.3.4')
        #c.close()

    # CURLOPT_POSTREDIR was introduced in libcurl-7.19.1
    @util.min_libcurl(7, 19, 1)
    def test_postredir(self):
        assert hasattr(pycurl, 'POSTREDIR')
        assert hasattr(pycurl, 'REDIR_POST_301')
        assert hasattr(pycurl, 'REDIR_POST_302')
        assert hasattr(pycurl, 'REDIR_POST_ALL')
    
    # CURLOPT_POSTREDIR was introduced in libcurl-7.19.1
    @util.min_libcurl(7, 19, 1)
    def test_postredir_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.POSTREDIR, curl.REDIR_POST_301)
        curl.close()
    
    # CURL_REDIR_POST_303 was introduced in libcurl-7.26.0
    @util.min_libcurl(7, 26, 0)
    def test_redir_post_303(self):
        assert hasattr(pycurl, 'REDIR_POST_303')

    # CURLOPT_POSTREDIR was introduced in libcurl-7.19.1
    @util.min_libcurl(7, 19, 1)
    def test_postredir_flags(self):
        self.assertEqual(pycurl.REDIR_POST_301, pycurl.REDIR_POST_ALL & pycurl.REDIR_POST_301)
        self.assertEqual(pycurl.REDIR_POST_302, pycurl.REDIR_POST_ALL & pycurl.REDIR_POST_302)

    # CURL_REDIR_POST_303 was introduced in libcurl-7.26.0
    @util.min_libcurl(7, 26, 0)
    def test_postredir_post_303(self):
        self.assertEqual(pycurl.REDIR_POST_303, pycurl.REDIR_POST_ALL & pycurl.REDIR_POST_303)

    # HTTPAUTH_DIGEST_IE was introduced in libcurl-7.19.3
    @util.min_libcurl(7, 19, 3)
    def test_httpauth_digest_ie(self):
        assert hasattr(pycurl, 'HTTPAUTH_DIGEST_IE')

    # CURLE_OPERATION_TIMEDOUT was introduced in libcurl-7.10.2
    # to replace CURLE_OPERATION_TIMEOUTED
    def test_operation_timedout_constant(self):
        self.assertEqual(pycurl.E_OPERATION_TIMEDOUT, pycurl.E_OPERATION_TIMEOUTED)
    
    # CURLOPT_NOPROXY was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    def test_noproxy_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.NOPROXY, 'localhost')
        curl.close()
    
    # CURLOPT_PROTOCOLS was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    def test_protocols_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.PROTOCOLS, curl.PROTO_ALL & ~curl.PROTO_HTTP)
        curl.close()
    
    # CURLOPT_REDIR_PROTOCOLS was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    def test_redir_protocols_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.PROTOCOLS, curl.PROTO_ALL & ~curl.PROTO_HTTP)
        curl.close()
    
    # CURLOPT_TFTP_BLKSIZE was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    def test_tftp_blksize_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.TFTP_BLKSIZE, 1024)
        curl.close()
    
    # CURLOPT_SOCKS5_GSSAPI_SERVICE was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    @nose.plugins.attrib.attr('gssapi')
    def test_socks5_gssapi_service_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SOCKS5_GSSAPI_SERVICE, 'helloworld')
        curl.close()
    
    # CURLOPT_SOCKS5_GSSAPI_NEC was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    @nose.plugins.attrib.attr('gssapi')
    def test_socks5_gssapi_nec_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SOCKS5_GSSAPI_NEC, True)
        curl.close()
    
    # CURLPROXY_HTTP_1_0 was introduced in libcurl-7.19.4
    @util.min_libcurl(7, 19, 4)
    def test_curlproxy_http_1_0_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.PROXYTYPE, curl.PROXYTYPE_HTTP_1_0)
        curl.close()
    
    # CURLOPT_SSH_KNOWNHOSTS was introduced in libcurl-7.19.6
    @util.min_libcurl(7, 19, 6)
    @util.guard_unknown_libcurl_option
    def test_ssh_knownhosts_setopt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSH_KNOWNHOSTS, '/hello/world')
        curl.close()
    
    # CURLOPT_MAIL_FROM was introduced in libcurl-7.20.0
    @util.min_libcurl(7, 20, 0)
    def test_mail_from(self):
        curl = pycurl.Curl()
        curl.setopt(curl.MAIL_FROM, 'hello@world.com')
        curl.close()
    
    # CURLOPT_MAIL_RCPT was introduced in libcurl-7.20.0
    @util.min_libcurl(7, 20, 0)
    def test_mail_rcpt(self):
        curl = pycurl.Curl()
        curl.setopt(curl.MAIL_RCPT, ['hello@world.com', 'foo@bar.com'])
        curl.close()
    
    # CURLOPT_MAIL_AUTH was introduced in libcurl-7.25.0
    @util.min_libcurl(7, 25, 0)
    def test_mail_auth(self):
        curl = pycurl.Curl()
        curl.setopt(curl.MAIL_AUTH, 'hello@world.com')
        curl.close()
    
    @util.min_libcurl(7, 22, 0)
    @nose.plugins.attrib.attr('gssapi')
    def test_gssapi_delegation_options(self):
        curl = pycurl.Curl()
        curl.setopt(curl.GSSAPI_DELEGATION, curl.GSSAPI_DELEGATION_FLAG)
        curl.setopt(curl.GSSAPI_DELEGATION, curl.GSSAPI_DELEGATION_NONE)
        curl.setopt(curl.GSSAPI_DELEGATION, curl.GSSAPI_DELEGATION_POLICY_FLAG)
        curl.close()
    
    # SSLVERSION_DEFAULT causes CURLE_UNKNOWN_OPTION without SSL
    @util.only_ssl
    def test_sslversion_options(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_DEFAULT)
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_SSLv2)
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_SSLv3)
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_TLSv1)
        curl.close()
    
    @util.min_libcurl(7, 34, 0)
    # SSLVERSION_TLSv1_0 causes CURLE_UNKNOWN_OPTION without SSL
    @util.only_ssl
    def test_sslversion_7_34_0(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_TLSv1_0)
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_TLSv1_1)
        curl.setopt(curl.SSLVERSION, curl.SSLVERSION_TLSv1_2)
        curl.close()
    
    @util.min_libcurl(7, 41, 0)
    @util.only_ssl_backends('openssl', 'nss')
    def test_ssl_verifystatus(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_VERIFYSTATUS, True)
        curl.close()
    
    @util.min_libcurl(7, 43, 0)
    @nose.plugins.attrib.attr('gssapi')
    def test_proxy_service_name(self):
        curl = pycurl.Curl()
        curl.setopt(curl.PROXY_SERVICE_NAME, 'fakehttp')
        curl.close()
    
    @util.min_libcurl(7, 43, 0)
    @nose.plugins.attrib.attr('gssapi')
    def test_service_name(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SERVICE_NAME, 'fakehttp')
        curl.close()
    
    @util.min_libcurl(7, 39, 0)
    def test_pinnedpublickey(self):
        curl = pycurl.Curl()
        curl.setopt(curl.PINNEDPUBLICKEY, '/etc/publickey.der')
        curl.close()
    
    @util.min_libcurl(7, 21, 0)
    def test_wildcardmatch(self):
        curl = pycurl.Curl()
        curl.setopt(curl.WILDCARDMATCH, '*')
        curl.close()
    
    @util.min_libcurl(7, 40, 0)
    def test_unix_socket_path(self):
        curl = pycurl.Curl()
        curl.setopt(curl.UNIX_SOCKET_PATH, '/tmp/socket.sock')
        curl.close()
    
    @util.min_libcurl(7, 36, 0)
    def test_ssl_enable_alpn(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_ENABLE_ALPN, 1)
        curl.close()
    
    @util.min_libcurl(7, 36, 0)
    def test_ssl_enable_npn(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_ENABLE_NPN, 1)
        curl.close()
    
    @util.min_libcurl(7, 42, 0)
    @util.only_ssl_backends('nss')
    def test_ssl_falsestart(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_FALSESTART, 1)
        curl.close()
    
    def test_ssl_verifyhost(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.close()
    
    def test_cainfo(self):
        curl = pycurl.Curl()
        curl.setopt(curl.CAINFO, '/bogus-cainfo')
        curl.close()

    @util.only_ssl
    def test_issuercert(self):
        curl = pycurl.Curl()
        curl.setopt(curl.ISSUERCERT, '/bogus-issuercert')
        curl.close()
    
    @util.only_ssl
    def test_capath(self):
        curl = pycurl.Curl()
        curl.setopt(curl.CAPATH, '/bogus-capath')
        curl.close()
    
    @util.only_ssl
    def test_crlfile(self):
        curl = pycurl.Curl()
        curl.setopt(curl.CRLFILE, '/bogus-crlfile')
        curl.close()
    
    @util.only_ssl
    def test_random_file(self):
        curl = pycurl.Curl()
        curl.setopt(curl.RANDOM_FILE, '/bogus-random')
        curl.close()

    @util.only_ssl_backends('openssl', 'gnutls')
    def test_egdsocket(self):
        curl = pycurl.Curl()
        curl.setopt(curl.EGDSOCKET, '/bogus-egdsocket')
        curl.close()
    
    @util.only_ssl
    def test_ssl_cipher_list(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_CIPHER_LIST, 'RC4-SHA:SHA1+DES')
        curl.close()
    
    @util.only_ssl
    def test_ssl_sessionid_cache(self):
        curl = pycurl.Curl()
        curl.setopt(curl.SSL_SESSIONID_CACHE, True)
        curl.close()
    
    def test_krblevel(self):
        curl = pycurl.Curl()
        curl.setopt(curl.KRBLEVEL, 'clear')
        curl.close()
    
    def test_krb4level(self):
        curl = pycurl.Curl()
        curl.setopt(curl.KRB4LEVEL, 'clear')
        curl.close()
