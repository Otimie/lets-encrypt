import certbot.main

def handler(event, context):
    certbot.main.main([
        'certonly',                             # Obtain a cert but don't install it
        '-n',                                   # Run in non-interactive mode
        '--agree-tos',                          # Agree to the terms of service,
        '--email', 'contact@lachlanb.me',       # Email
        '--dns-cloudflare',                     # Use dns challenge with cloudflare
        '--dns-cloudflare-credentials', 'cloudflare.ini',
        '-d', 'lachlanb.me',                    # Domains to provision certs for
        # Override directory paths so script doesn't have to be run as root
        '--config-dir', '/tmp/config-dir/',
        '--work-dir', '/tmp/work-dir/',
        '--logs-dir', '/tmp/logs-dir/',
    ])
    
handler('', '')
