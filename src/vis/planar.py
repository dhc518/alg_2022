import math
from vis.base import *

# t = 0.0 ~ 2.0 사이로 변화하는 값임. 1 이면 가운데임
def lerp_2d(xy1, xy2, t=1):
  # x1,y1 = xy1[0], xy1[1]
  # x2,y2 = xy2[0], xy2[1]
  x1,y1,x2,y2 = *xy1, *xy2
  return [(x1*(2-t)+x2*t)//2, (y1*(2-t)+y2*t)//2]

# 평면 시각화
class PlanarVisualizer(Visualizer):
  def_city_context = {
    'city_body_color': Color.LightBlue,
    'city_line_color': Color.DeepSkyBlue,
    'city_name_color': Color.DarkBlue,
    # 'shows_city_index': True,
    # 'shows_city_coord': True,
  }
  def_edge_context = {
    'edge_line_color': Color.Teal,
    'edge_value_color': Color.DarkGreen,
  }

  def setup(self, data):
    self.data = data
    self.compute_min_max()
    self.city_contexts = dict()
    self.edge_contexts = dict()
    self.legend_right = self.separator_size
    self.legend_bottom = self.separator_size
    # self.draw()

  def compute_min_max(self):
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    for c in self.data.cities:
      if min_x > c.x: min_x = c.x
      if min_y > c.y: min_y = c.y
      if max_x < c.x: max_x = c.x
      if max_y < c.y: max_y = c.y
    self.min_x, self.max_x = min_x, max_x
    self.min_y, self.max_y = min_y, max_y

    self.diff_x = max_x - min_x
    self.diff_y = max_y - min_y

  def get_city_context(self, index):
    if index in self.city_contexts:
      return self.city_contexts[index]
    return None

  def set_city_context(self, index, context=None):
    if context == None:
      if index in self.city_contexts:
        del self.city_contexts[index]
    else:
      self.city_contexts[index] = context

  def get_edge_context(self, u,v):
    if u > v: u,v = v,u
    if (u,v) in self.edge_contexts:
      return self.edge_contexts[(u,v)]
    return None

  def set_edge_context(self, u,v, context):
    if u > v: u,v = v,u
    if context == None:
      del self.edge_contexts[index]
    else:
      self.edge_contexts[(u,v)] = context

  def draw(self):
    self.clear()
    self.calc_coords()
    self.draw_content()
    self.update_display()

  def draw_content(self):
    if hasattr(self.data, 'edges'):
      self.draw_all_edges()
    self.draw_all_cities()

  def calc_coords(self):
    cw = self.config.screen_width - self.separator_size - self.legend_right
    ch = self.config.screen_height - self.separator_size - self.legend_bottom

    scale_x, scale_y = cw / self.diff_x, ch / self.diff_y
    if scale_x < scale_y:
      self.scale = scale_x
      self.diff = self.diff_x
    else:
      self.scale = scale_y
      self.diff = self.diff_y

    self.city_radius = self.config.font_size // 3

  def o2s(self, x, y):
    dx, dy = x - self.min_x, y - self.min_y
    x = self.separator_size + dx * self.scale
    y = self.separator_size + dy * self.scale
    return [x, y]

  def xy2s(self, xy):
    return self.o2s(xy[0], xy[1])

  def city2s(self, city):
    return self.xy2s([city.x, city.y])

  def draw_all_cities(self, **args):
    uses_ctx = len(args) == 0
    for i in range(len(self.data.cities)):
      if uses_ctx:
        ctx = self.get_city_context(i)
        if not ctx: ctx = self.def_city_context
      else:
        ctx = args
      self.draw_city(i, **ctx)

  def draw_all_edges(self, **args):
    uses_ctx = len(args) == 0
    for u,v,w in self.data.edges:
      if uses_ctx:
        ctx = self.get_edge_context(u, v)
        if not ctx: ctx = self.def_edge_context
      else:
        ctx = args
      self.draw_edge(u,v,w, **ctx)

  def draw_city(self, city, **args):
    if isinstance(city, int):
      city = self.data.cities[city]
    xy = self.xy2s([city.x, city.y])
    body_color = attr(args, 'city_body_color', Color.back)
    line_color = attr(args, 'city_line_color', Color.line)
    name_color = attr(args, 'city_name_color', Color.text)

    # def_city_context = {
    #   'city_body_color': Color.DeepSkyBlue,
    #   'city_line_color': Color.LightBlue,
    #   'city_name_color': Color.DarkBlue,

    radius = self.city_radius
    pg.draw.circle(self.screen, body_color, xy, radius)
    pg.draw.circle(self.screen, line_color, xy, radius, 1)

    xy[1] -= self.config.font_size // 2 + radius
    name = city.getName(**args)

    self.draw_text(name, xy, text_color=name_color, **args)

  def draw_edge(self, c1, c2, value=None, **args):
    if isinstance(c1, int): c1 = self.data.cities[c1]
    if isinstance(c2, int): c2 = self.data.cities[c2]
    xy1, xy2 = self.city2s(c1), self.city2s(c2)
    line_color = attr(args, 'edge_line_color', Color.line)
    thickness = attr(args, 'edge_line_width', 1)
    if thickness == 1:
      pg.draw.aaline(self.screen, line_color, xy1, xy2)
    else:
      pg.draw.line(self.screen, line_color, xy1, xy2, thickness)
    if value != None:
      shows_value = attr(args, 'shows_edge_value', False)
      if shows_value:
        xy = lerp_2d(xy1, xy2)
        value_color = attr(args, 'edge_value_color', Color.text)
        self.draw_text(f'{value}', xy, text_color=value_color)

  def draw_directed_edge(self, c1, c2, value=None, **args):
    if isinstance(c1, int): c1 = self.data.cities[c1]
    if isinstance(c2, int): c2 = self.data.cities[c2]
    x1,y1,x2,y2 = *self.city2s(c1), *self.city2s(c2)
    angle = math.atan2(y2-y1, x2-x1)
    shift_angle = angle + math.pi / 2
    radius = self.city_radius // 2
    shift_x = radius * math.cos(shift_angle)
    shift_y = radius * math.sin(shift_angle)
    sxy, dxy = self.shorter_line(x1+shift_x, y1+shift_y, x2+shift_x, y2+shift_y, angle)
    self.draw_arrow(sxy, dxy, angle, value, **args)

  def draw_arrow(self, sxy, dxy, angle=None, value=None, **args):
    line_color = attr(args, 'edge_line_color', Color.line)
    axy = self.get_arrow_pos(sxy, dxy, angle)
    pg.draw.aaline(self.screen, line_color, sxy, dxy)
    pg.draw.aaline(self.screen, line_color, dxy, axy)

    if value != None:
      shows_value = attr(args, 'shows_edge_value', False)
      if shows_value:
        xy = lerp_2d(sxy, dxy, 1.1) # at 55% position (1=50%, 2=100%)
        value_color = attr(args, 'edge_value_color', Color.line)
        self.draw_text(f'{value}', xy, text_color=value_color)

  def shorter_line(self, x1,y1,x2,y2,angle=None):
    diff = 2 * self.city_radius
    if angle == None:
      angle = math.atan2(y2-y1, x2-x1)
    dx = diff * math.cos(angle)
    dy = diff * math.sin(angle)
    return [x1+dx,y1+dy], [x2-dx,y2-dy]

  def get_arrow_pos(self, xy1, xy2, angle=None):
    length = 2 * self.city_radius
    x1,y1 = xy1
    x2,y2 = xy2
    if angle == None:
      angle = math.atan2(y2-y1, x2-x1)
    angle += math.pi * 5 / 6 # 150 degree
    ax = x2 + length * math.cos(angle)
    ay = y2 + length * math.sin(angle)
    return [ax, ay]


class KruskalVisualizer(PlanarVisualizer):
  normal_city_context = {
    'city_body_color': Color.LightBlue,
    'city_line_color': Color.DeepSkyBlue,
    'city_name_color': Color.DarkBlue,
    'shows_city_index': True,
    # 'shows_city_coord': True,
  }
  def_city_context = normal_city_context
  grayed_edge_context = {
    'edge_line_color': Color.WhiteSmoke,
    'edge_value_color': Color.WhiteSmoke,
    'shows_edge_value': True,
  }
  def_edge_context = {
    'edge_line_color': Color.Teal,
    'edge_value_color': Color.DarkGreen,
    'shows_edge_value': True,
  }
  ectx_ignore = {
    'edge_line_color': Color.Crimson,
    'edge_value_color': Color.DarkRed,
    'edge_line_width': 5,
    'shows_edge_value': True,
  }
  bctx_current = {
    'body_color': Color.LightSalmon,
    'line_color': Color.DarkRed,
    'text_color': Color.Indigo,
  }

  def setup(self, data):
    super().setup(data)
    self.candidates = []
    self.max_weight = max(e[2] for e in data.edges)
    self.appended_edge = (-1, -1)

  def calc_coords(self):
    self.legend_right = self.config.screen_width // 3
    self.legend_bottom = self.config.screen_height // 3

    super().calc_coords()

    self.weights_y = self.config.screen_height - self.legend_bottom + self.separator_size
    self.weights_w = self.config.screen_width - self.legend_right - self.separator_size
    self.weights_h = self.legend_bottom - 2 * self.separator_size

    self.roots_x = self.config.screen_width - self.legend_right + self.separator_size
    self.roots_w = self.legend_right - 2 * self.separator_size
    self.roots_x2 = self.roots_x + self.roots_w // 2
    self.roots_y = self.separator_size
    self.roots_h = self.config.screen_height - 2 * self.separator_size
    self.root_h = max(self.config.font_size, self.roots_h // len(self.data.cities))

  def draw_content(self):
    if hasattr(self.data, 'edges'):
      self.draw_all_edges()
    self.draw_all_cities(**self.def_city_context)

    self.draw_candidates()
    self.draw_right_pane()

  def get_edge_context(self, u,v):
    if u > v: u,v = v,u
    if (u,v) in self.candidates:
      return self.grayed_edge_context
    return super().get_edge_context(u, v)

  def sort_edges(self):
    self.candidates = []
    self.weights = dict()
    max_weight = 0
    for u,v,w in self.data.edges:
      if u > v: u,v = v,u
      self.candidates.append((u,v))
      self.weights[(u,v)] = w
      if max_weight < w:
        max_weight = w
      self.draw()
      self.wait(100)
    self.max_weight = max_weight

  def draw_candidates(self):
    x = self.separator_size
    y = self.weights_y
    legend = self.weights_h
    ix = self.weights_w // len(self.data.edges)
    for u,v,w in self.data.edges:
      if u > v: u,v = v,u
      if (u,v) in self.candidates:
        color = Color.Crimson
      else:
        color = Color.WhiteSmoke
      height = legend * w / self.max_weight
      pg.draw.line(self.screen, color, [x,y], [x,y+height])
      x += ix

  def append(self, u, v, w):
    if u > v: u,v = v,u
    if (u,v) in self.candidates:
      del self.candidates[self.candidates.index((u,v))]

    self.appended_edge = (u,v)
    self.draw()
    self.wait(1000)

  def ignore(self, u, v, w):
    if u > v: u,v = v,u
    self.draw()
    self.draw_edge(u, v, w, **self.ectx_ignore)
    self.update_display()
    self.wait(1000)

  def draw_right_pane(self):
    if not hasattr(self.data, 'roots'): return

    x = self.roots_x
    y = self.roots_y
    w = self.roots_w
    h = self.root_h
    u,v = self.appended_edge
    for i in range(len(self.data.roots)):
      r = self.data.roots[i]
      ci = self.data.cities[i]
      cr = self.data.cities[r]
      if i == v:
        ctx = self.bctx_current
      else:
        ctx = {}
      self.draw_box([x,y,w,h], text=f'{ci.index}.{ci.name} - {cr.index}.{cr.name}', **ctx)
      y += h

  def finish(self):
    self.appended_edge = -1, -1
    self.draw()

class PrimVisualizer(KruskalVisualizer):
  grayed_city_context = {
    'city_body_color': Color.WhiteSmoke,
    'city_line_color': Color.LightGray,
    'city_name_color': Color.LightGray,
    'shows_city_index': True,
    # 'shows_city_coord': True,
  }
  candidate_city_context = {
    'city_body_color': Color.PaleGreen,
    'city_line_color': Color.Magenta,
    'city_name_color': Color.SkyBlue,
    'shows_city_index': True,
    # 'shows_city_coord': True,
  }
  candidate_edge_context = {
    'edge_line_color': Color.LightGray,
    'edge_value_color': Color.SkyBlue,
    'shows_edge_value': True,
  }
  bctx_updated = {
    'body_color': Color.LightGreen,
    'line_color': Color.DarkGreen,
    'text_color': Color.text,
  }
  def_city_context = grayed_city_context
  def_edge_context = KruskalVisualizer.grayed_edge_context
  fixed_edge_context = KruskalVisualizer.def_edge_context
  fixing_edge_context = {
    'edge_line_color': Color.Crimson,
    'edge_value_color': Color.DarkRed,
    'shows_edge_value': True,
    'edge_line_width': 5,
  }
  compare_edge_context = {
    'edge_line_color': Color.LightGreen,
    'edge_value_color': Color.DarkGreen,
    'shows_edge_value': True,
    'edge_line_width': 5,
  }


  def setup(self, data):
    super().setup(data)
    self.weights = []
    self.connections = dict()
    self.push_index = -1
    self.pop_index = -1
    self.update_index = -1
    self.fixing_index = -1
    self.current_index = -1

  def draw_content(self):
    if hasattr(self.data, 'edges'):
      self.draw_all_edges()
    self.draw_all_cities()

    self.draw_candidates()
    self.draw_right_pane()

  def draw_right_pane(self):
    bx = self.roots_x
    y = self.roots_y
    w = self.roots_w
    h = self.root_h
    u,v = self.appended_edge
    animates_y = False
    for weight, ci in self.weights:
      city = self.data.cities[ci]
      text = f'{weight} - {city.index}.{city.name}'
      ctx = {}#self.bctx_current
      x = bx
      if ci == self.push_index:
        x += (1 - self.anim_progress) * self.roots_w
      elif ci == self.pop_index:
        x += (self.anim_progress) * self.roots_w
        animates_y = True
      elif ci == self.update_index:
        ctx = self.bctx_updated
      elif ci == self.fixing_index:
        ctx = self.bctx_current

      ty = y
      if animates_y and ci != self.pop_index: ty -= self.anim_progress * h
      self.draw_box([x,ty,w,h], text=text, **ctx)
      y += h

  def draw_city(self, city, **args):
    if city == self.current_index:
      radius = self.config.font_size
      c = self.data.cities[city]
      pg.draw.circle(self.screen, Color.line, self.city2s(c), radius, 1)
    super().draw_city(city, **args)

  # def get_edge_context(self, u,v):

  def append(self, weight, ci, c2=None):
    self.set_city_context(ci, self.candidate_city_context)
    if c2 != None:
      self.connections[ci] = c2
      self.set_edge_context(ci, c2, self.candidate_edge_context)
    self.weights.append((weight, ci))
    self.push_index = ci
    # msec = 1000 if c2 == None else 500
    self.animate(1000)
    self.push_index = -1

  def update(self, weight, ci, ci_from):
    print('update', weight, ci)
    for i in range(len(self.weights)):
      w, c = self.weights[i]
      if c == ci:
        wi = i
        break
    else: return

    ci_orig = self.connections[ci]
    self.set_edge_context(ci, ci_from, self.candidate_edge_context)
    self.set_edge_context(ci, ci_orig, self.compare_edge_context)
    self.update_index = ci
    self.weights[wi] = (weight, ci)
    self.draw()
    self.wait(1000)
    self.update_index = -1
    self.set_edge_context(ci, ci_orig, self.grayed_edge_context)
    self.draw()

  def fix(self, ci, ci_from=None):
    self.current_index = ci
    self.connections[ci_from] = ci
    if ci != ci_from:
      self.fixing_index = ci
      self.set_edge_context(ci_from, ci, self.fixing_edge_context)
      self.draw()
      self.wait(1000)
      self.fixing_index = -1
      self.set_edge_context(ci_from, ci, self.fixed_edge_context)
    self.set_city_context(ci, self.normal_city_context)
    self.pop_index = ci
    self.animate(1000)
    self.pop_index = -1
    for i in range(len(self.weights)):
      if self.weights[i][1] == ci:
        self.weights.pop(i)
        break
    self.draw()

  def compare(self, ci, ci_from):
    self.update_index = ci
    self.set_edge_context(ci_from, ci, self.compare_edge_context)
    self.draw()
    self.wait(1000)
    self.update_index = -1
    self.set_edge_context(ci_from, ci, self.grayed_edge_context)
    self.draw()



