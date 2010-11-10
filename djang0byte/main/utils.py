# -*- coding: utf-8 -*-
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.



def file_upload_path(instance, filename):
    """Generates upload path
    
    Keyword arguments:
    instance -- FileField
    filename - String
    
    Returns: String
    
    """
    parts = filename.rsplit('.', 1)
    str = "%s.%s" % (slugify(translify(parts[0])), slugify(translify(parts[1])))
    return "%s/%s/%s/%s" % (strftime('%Y'), 
       strftime('%m'), strftime('%d'), str)

class Access:
    newPost = 0
    newBlog = 1
    newComment = 2
    ratePost = 3
    rateComment = 4
    rateUser = 5
    rateBlog = 6