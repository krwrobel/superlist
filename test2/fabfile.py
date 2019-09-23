from fabric import Connection
result = Connection('superlist-staging.wblkrzysztof.site').run('uname -s', hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"

print(msg)