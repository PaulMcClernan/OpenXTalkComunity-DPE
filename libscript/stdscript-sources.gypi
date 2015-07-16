{
	'variables':
	{
		# Source LCB files for the stdscript library containing syntax
		'stdscript_syntax_lcb_files':
		[
			'src/arithmetic.mlc',
			'src/array.mlc',
			'src/binary.mlc',
			'src/bitwise.mlc',
			'src/byte.mlc',
			'src/char.mlc',
			'src/codeunit.mlc',
			'src/date.mlc',
			#'src/encoding.mlc',
			'src/file.mlc',
			'src/foreign.mlc',
			#'src/item.mlc',
			#'src/line.mlc',
			'src/list.mlc',
			'src/logic.mlc',
			#'src/map.mlc',
			'src/math.mlc',
			'src/math-foundation.mlc',
			#'src/segmentchunk.mlc',
			'src/sort.mlc',
			'src/stream.mlc',
			'src/string.mlc',
			'src/system.mlc',
			'src/type.mlc',
			'src/type-convert.mlc',
			'src/unittest.mlc',
			#'src/url.mlc',
		],
		
		'stdscript_other_lcb_files':
		[
			'src/unittest-impl.mlc',
		],
		
		'stdscript_sources':
		[
			'src/module-arithmetic.cpp',
			'src/module-array.cpp',
			'src/module-binary.cpp',
			'src/module-bitwise.cpp',
			'src/module-byte.cpp',
			'src/module-char.cpp',
			'src/module-codeunit.cpp',
			'src/module-date.cpp',
			'src/module-encoding.cpp',
			'src/module-file.cpp',
			'src/module-foreign.cpp',
			'src/module-list.cpp',
			'src/module-logic.cpp',
			'src/module-map.cpp',
			'src/module-math_foundation.cpp',
			'src/module-math.cpp',
			'src/module-sort.cpp',
			'src/module-stream.cpp',
			'src/module-string.cpp',
			'src/module-system.cpp',
			'src/module-type_convert.cpp',
			'src/module-type.cpp',
			'src/module-unittest.cpp',
			'src/module-unittest_IMPL.cpp',
			'src/module-url.cpp',
		],
	},
}
