#define sprintf(%1)                         (format(g_szSprintfBuffer, sizeof(g_szSprintfBuffer), %1), g_szSprintfBuffer)

stock g_szSprintfBuffer[ 1024 ];

// purpose: set a server rule
stock SetServerRule( const rule[ ], const value[ ] ) {
	return SendRconCommand( sprintf( "%s %s", rule, value ) );
}