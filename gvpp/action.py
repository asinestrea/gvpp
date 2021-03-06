# Copyright 2016, Sinestrea <git.sinestrea@gmail.com>
#
# This file is part of "gvpp".
#
# "gvpp" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# "gvpp" is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# "gvpp". If not, see <http://www.gnu.org/licenses/>.

class NextStep( object ):
	def __init__( self, clean = False ):
		self.clean = clean
	def __call__( self, steps ):
		from gvpp.animation import Step
		steps.append( Step( None if self.clean else steps[ -1 ] ) )

class AddNode( object ):
	def __init__( self, v, gvfmt ):
		self.v = v
		self.gvfmt = gvfmt
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].gvfV[ self.v ] = self.gvfmt

class GvFormatNode( object ):
	def __init__( self, v, fmt = 'shape=oval' ):
		self.v = v
		self.fmt = fmt
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].gvfV[ self.v ] = self.fmt

class HighlightNode( object ):
	def __init__( self, v, color = 'red' ):
		self.v = v
		self.color = color
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].hV[ self.v ] = self.color

class LabelNode( object ):
	def __init__( self, v, label ):
		self.v = v
		self.label = label
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].lV[ self.v ] = self.label

class UnlabelNode( object ):
	def __init__( self, v ):
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.v )
		try:
			del steps[ -1 ].lV[ self.v ]
		except KeyError:
			pass

class RemoveNode( object ):
	def __init__( self, v ):
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.discard( self.v )
		try:
			del steps[ -1 ].hV[ self.v ]
		except KeyError:
			pass
		try:
			del steps[ -1 ].lV[ self.v ]
		except KeyError:
			pass
		dE = set( e for e in steps[ -1 ].E if self.v in e )
		steps[ -1 ].E -= dE
		for e in list(steps[ -1 ].hE.keys()):
			if self.v in e:
				del steps[ -1 ].hE[ e ]

class AddEdge( object ):
	def __init__( self, u, v ):
		self.u = u
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.u )
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].E.add( ( self.u, self.v ) )

class HighlightEdge( object ):
	def __init__( self, u, v, color = 'red' ):
		self.u = u
		self.v = v
		self.color = color
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.u )
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].E.add( ( self.u, self.v ) )
		steps[ -1 ].hE[ ( self.u, self.v ) ] = self.color

class LabelEdge( object ):
	def __init__( self, u, v, label ):
		self.u = u
		self.v = v
		self.label_edge = label
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.u )
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].E.add( ( self.u, self.v ) )
		steps[ -1 ].lE[ ( self.u, self.v ) ] = self.label_edge

class UnlabelEdge( object ):
	def __init__( self, u, v ):
		self.u = u
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].V.add( self.u )
		steps[ -1 ].V.add( self.v )
		steps[ -1 ].E.add( ( self.u, self.v ) )
		try:
			del steps[ -1 ].lE[ ( self.u, self.v ) ]
		except KeyError:
			pass

class RemoveEdge( object ):
	def __init__( self, u, v ):
		self.u = u
		self.v = v
	def __call__( self, steps ):
		steps[ -1 ].E.discard( ( self.u, self.v ) )
		try:
			del steps[ -1 ].hE[ ( self.u, self.v ) ]
			del steps[ -1 ].lE[ ( self.u, self.v ) ]
		except KeyError:
			pass
