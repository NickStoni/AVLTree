from PIL import Image, ImageDraw
import VisualiserConfig as cfg

"""TreeVisualiser is a class which implements representing
the internal structure of the tree visually as an image,
with draw_tree being the main function."""
class TreeVisualiser:
    def __init__(self, tree):
        self.tree = tree
        self.image = Image.new(mode=cfg.MODE, size=(cfg.SIZE, cfg.SIZE))
        self.draw = ImageDraw.Draw(self.image)
        self.node_radius = None
        self.y_shift = None
        self.max = None

    #draw_tree - The main function of the TreeVisualiser class, which creates and saves the image
    def draw_tree(self):
        self.node_radius = self.calculate_radius()
        self.rel_y_shift = self.get_rel_y_shift(self.node_radius)

        height = self.tree.root.height
        self.max = self.calculate_max(height)

        x_initial_rel = 0.5
        y_initial_rel = 0

        self.execute_draw_tree(self.tree.root, height, x_initial_rel, y_initial_rel)
        self.image.save("{}.png".format(cfg.NAME))

    #execute_draw_tree - A recursive helper function, which draws individual nodes
    def execute_draw_tree(self, node, height, x_rel, y_rel):
        if node is None:
            return

        x_coord = x_rel * cfg.SIZE
        y_coord = y_rel * cfg.SIZE
        x_rel_shift = self.get_rel_x_shift(height, self.max)
        adjustment = self.node_radius//2

        self.draw_node(node.data, x_coord, y_coord, self.node_radius)

        if node.left is not None:
            from_coords = (x_coord + adjustment, y_coord + adjustment)
            to_coords = ((x_rel - x_rel_shift) * cfg.SIZE + adjustment,
                         (y_rel + self.rel_y_shift) * cfg.SIZE + adjustment)

            self.draw_line(from_coords, to_coords)
            self.execute_draw_tree(node.left, height - 1, x_rel - x_rel_shift, y_rel + self.rel_y_shift)

        if node.right is not None:
            from_coords = (x_coord + adjustment, y_coord + adjustment)
            to_coords = ((x_rel + x_rel_shift) * cfg.SIZE + adjustment,
                         (y_rel + self.rel_y_shift) * cfg.SIZE + adjustment)

            self.draw_line(from_coords, to_coords)
            self.execute_draw_tree(node.right, height - 1, x_rel + x_rel_shift, y_rel + self.rel_y_shift)

        self.draw_node(node.data, x_coord, y_coord, self.node_radius)

    #draw_line - A helper function, which draws line from and to given coordinates
    def draw_line(self, from_coords, to_coords):
        self.draw.line((from_coords, to_coords), fill=cfg.LINE_COLOR, width=cfg.LINE_WIDTH)

    #draw_node - A helper function, which draws and individual node, given coordinates and radius
    def draw_node(self, data, x, y, radius):
        adjustment = radius//4
        self.draw.ellipse((x, y, x + radius, y + radius), fill=cfg.FILL_COLOR, outline=cfg.OUTLINE_COLOR)
        self.draw.text((x + adjustment, y + adjustment), str(data))

    #calculate_radius - A helper function, which calculates radius for nodes
    def calculate_radius(self):
        levels = self.tree.root.height
        max_level_nodes = 2**levels
        radius = cfg.SIZE - cfg.RELATIVE_GAP * cfg.SIZE * (max_level_nodes - 1) / max_level_nodes

        return min(radius, cfg.RADIUS_LIMIT)

    #get_rel_x_shift - A helper function, which calculates the relative shift in x coordinate
    #when drawing the children of a node
    def get_rel_x_shift(self, height, max):
        return 2 ** (height - 2) / max

    #calculate_max - A helper function, which is used to calculate "max" used in get_rel_x_shift
    def calculate_max(self, n):
        if n == 0:
            return 1

        return 2 * self.calculate_max(n - 1) + 1

    #get_rel_y_shift - A helper function, which is used to calculate the relative shift in y coordinate
    def get_rel_y_shift(self, radius):
        levels = self.tree.root.height
        shift = (cfg.SIZE - (levels + 1) * radius) / ( (levels-1) * cfg.SIZE) if levels != 1 else 0
        return shift