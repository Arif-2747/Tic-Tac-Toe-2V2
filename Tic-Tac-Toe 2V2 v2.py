import tkinter as tk
from tkinter import messagebox, font
import random

class ModernTicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Modern Tic Tac Toe")
        self.window.geometry("500x650")
        self.window.resizable(False, False)
        
        # Modern color scheme
        self.colors = {
            'bg': '#1a1a2e',
            'secondary': '#16213e',
            'accent': '#0f3460',
            'primary': '#e94560',
            'text': '#ffffff',
            'button': '#16213e',
            'button_hover': '#0f3460',
            'x_color': '#ff6b6b',
            'o_color': '#4ecdc4',
            'win_color': '#ffd93d'
        }
        
        self.window.configure(bg=self.colors['bg'])
        
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.score_x = 0
        self.score_o = 0
        
        self.setup_fonts()
        self.setup_ui()
        self.add_animations()
    
    def setup_fonts(self):
        self.title_font = font.Font(family="Helvetica", size=28, weight="bold")
        self.player_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=36, weight="bold")
        self.score_font = font.Font(family="Helvetica", size=14)
        self.control_font = font.Font(family="Helvetica", size=12, weight="bold")
    
    def setup_ui(self):
        # Main container with gradient effect simulation
        main_frame = tk.Frame(self.window, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title with glow effect
        title_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        title_frame.pack(pady=(0, 20))
        
        title_label = tk.Label(title_frame, 
                              text="TIC TAC TOE", 
                              font=self.title_font,
                              fg=self.colors['primary'],
                              bg=self.colors['bg'])
        title_label.pack()
        
        subtitle = tk.Label(title_frame,
                           text="✨ Modern Edition ✨",
                           font=font.Font(family="Helvetica", size=12),
                           fg=self.colors['text'],
                           bg=self.colors['bg'])
        subtitle.pack()
        
        # Player indicator with modern styling
        player_frame = tk.Frame(main_frame, bg=self.colors['secondary'], relief='flat', bd=2)
        player_frame.pack(pady=(0, 20), fill=tk.X)
        
        self.player_label = tk.Label(player_frame, 
                                   text=f"Player {self.current_player}'s Turn", 
                                   font=self.player_font,
                                   fg=self.get_player_color(self.current_player),
                                   bg=self.colors['secondary'],
                                   pady=10)
        self.player_label.pack()
        
        # Game board with modern styling - proper 3x3 grid
        board_container = tk.Frame(main_frame, bg=self.colors['bg'])
        board_container.pack(pady=20)
        
        board_frame = tk.Frame(board_container, bg=self.colors['accent'], relief='solid', bd=2)
        board_frame.pack()
        
        # Configure grid weights for even spacing
        for i in range(3):
            board_frame.grid_rowconfigure(i, weight=1)
            board_frame.grid_columnconfigure(i, weight=1)
        
        # Create 3x3 grid with modern buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(board_frame, 
                                 text="", 
                                 font=self.button_font,
                                 width=6, 
                                 height=3,
                                 bg=self.colors['button'],
                                 fg=self.colors['text'],
                                 activebackground=self.colors['button_hover'],
                                 activeforeground=self.colors['text'],
                                 relief='solid',
                                 bd=1,
                                 cursor='hand2',
                                 command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j, padx=1, pady=1, sticky='nsew')
                self.buttons[i][j] = button
                
                # Add hover effects
                button.bind("<Enter>", lambda e, btn=button: self.on_button_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_button_hover(btn, False))
        
        # Score display with modern cards
        score_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        score_frame.pack(pady=20, fill=tk.X)
        
        # Player X score card
        x_card = tk.Frame(score_frame, bg=self.colors['secondary'], relief='flat', bd=2)
        x_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        tk.Label(x_card, text="Player X", font=self.score_font, 
                fg=self.colors['x_color'], bg=self.colors['secondary']).pack(pady=5)
        self.score_x_label = tk.Label(x_card, text="0", font=self.title_font,
                                     fg=self.colors['text'], bg=self.colors['secondary'])
        self.score_x_label.pack(pady=5)
        
        # Player O score card
        o_card = tk.Frame(score_frame, bg=self.colors['secondary'], relief='flat', bd=2)
        o_card.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        tk.Label(o_card, text="Player O", font=self.score_font,
                fg=self.colors['o_color'], bg=self.colors['secondary']).pack(pady=5)
        self.score_o_label = tk.Label(o_card, text="0", font=self.title_font,
                                     fg=self.colors['text'], bg=self.colors['secondary'])
        self.score_o_label.pack(pady=5)
        
        # Control buttons with modern styling
        control_frame = tk.Frame(main_frame, bg=self.colors['bg'])
        control_frame.pack(pady=20)
        
        new_game_btn = tk.Button(control_frame, 
                               text="🎮 New Game", 
                               font=self.control_font,
                               bg=self.colors['primary'],
                               fg=self.colors['text'],
                               activebackground='#d63851',
                               activeforeground=self.colors['text'],
                               relief='flat',
                               bd=0,
                               padx=20,
                               pady=10,
                               cursor='hand2',
                               command=self.new_game)
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(control_frame, 
                           text="❌ Quit", 
                           font=self.control_font,
                           bg=self.colors['accent'],
                           fg=self.colors['text'],
                           activebackground='#0d2a52',
                           activeforeground=self.colors['text'],
                           relief='flat',
                           bd=0,
                           padx=20,
                           pady=10,
                           cursor='hand2',
                           command=self.window.quit)
        quit_btn.pack(side=tk.LEFT, padx=10)
    
    def add_animations(self):
        # Add a subtle animation to the title
        self.animate_title()
    
    def animate_title(self):
        colors = [self.colors['primary'], '#ff8a95', self.colors['primary']]
        current_color = random.choice(colors)
        # This would be the title label - we'll just change color occasionally
        self.window.after(3000, self.animate_title)
    
    def get_player_color(self, player):
        return self.colors['x_color'] if player == 'X' else self.colors['o_color']
    
    def on_button_hover(self, button, entering):
        if button['state'] != 'disabled':
            if entering:
                button.config(bg=self.colors['button_hover'])
            else:
                button.config(bg=self.colors['button'])
    
    def make_move(self, row, col):
        if self.game_over or self.board[row][col] != '':
            return
        
        # Make the move with color coding
        self.board[row][col] = self.current_player
        player_color = self.get_player_color(self.current_player)
        
        self.buttons[row][col].config(text=self.current_player, 
                                    fg=player_color,
                                    bg=self.colors['secondary'],
                                    state="disabled")
        
        # Check for winner
        if self.check_winner():
            self.game_over = True
            winner = self.current_player
            if winner == 'X':
                self.score_x += 1
                self.score_x_label.config(text=str(self.score_x))
            else:
                self.score_o += 1
                self.score_o_label.config(text=str(self.score_o))
            
            self.highlight_winning_line()
            self.show_modern_message(f"🎉 Player {winner} Wins! 🎉", "Victory!")
            return
        
        # Check for tie
        if self.is_board_full():
            self.game_over = True
            self.show_modern_message("🤝 It's a Tie! 🤝", "Draw!")
            return
        
        # Switch players
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.player_label.config(text=f"Player {self.current_player}'s Turn",
                               fg=self.get_player_color(self.current_player))
    
    def show_modern_message(self, message, title):
        # Create a custom modern message box
        popup = tk.Toplevel(self.window)
        popup.title(title)
        popup.geometry("300x200")
        popup.configure(bg=self.colors['bg'])
        popup.resizable(False, False)
        
        # Center the popup
        popup.transient(self.window)
        popup.grab_set()
        
        # Get window position
        x = self.window.winfo_x() + (self.window.winfo_width() // 2) - 150
        y = self.window.winfo_y() + (self.window.winfo_height() // 2) - 100
        popup.geometry(f"300x200+{x}+{y}")
        
        # Content frame
        content_frame = tk.Frame(popup, bg=self.colors['secondary'], relief='flat', bd=5)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Message
        msg_label = tk.Label(content_frame, 
                           text=message,
                           font=font.Font(family="Helvetica", size=16, weight="bold"),
                           fg=self.colors['primary'],
                           bg=self.colors['secondary'],
                           wraplength=250)
        msg_label.pack(expand=True)
        
        # OK button
        ok_btn = tk.Button(content_frame,
                         text="✨ Awesome! ✨",
                         font=font.Font(family="Helvetica", size=12, weight="bold"),
                         bg=self.colors['primary'],
                         fg=self.colors['text'],
                         relief='flat',
                         bd=0,
                         padx=20,
                         pady=8,
                         cursor='hand2',
                         command=popup.destroy)
        ok_btn.pack(pady=10)
    
    def check_winner(self):
        # Check rows
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2] != ''):
                self.winning_line = [(i, 0), (i, 1), (i, 2)]
                return True
        
        # Check columns
        for j in range(3):
            if (self.board[0][j] == self.board[1][j] == self.board[2][j] != ''):
                self.winning_line = [(0, j), (1, j), (2, j)]
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ''):
            self.winning_line = [(0, 0), (1, 1), (2, 2)]
            return True
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] != ''):
            self.winning_line = [(0, 2), (1, 1), (2, 0)]
            return True
        
        return False
    
    def highlight_winning_line(self):
        if hasattr(self, 'winning_line'):
            for row, col in self.winning_line:
                self.buttons[row][col].config(bg=self.colors['win_color'],
                                            fg=self.colors['bg'])
    
    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True
    
    def new_game(self):
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        # Reset all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", 
                                        bg=self.colors['button'],
                                        fg=self.colors['text'],
                                        state="normal")
        
        # Update player label
        self.player_label.config(text=f"Player {self.current_player}'s Turn",
                               fg=self.get_player_color(self.current_player))
        
        # Clear winning line
        if hasattr(self, 'winning_line'):
            delattr(self, 'winning_line')
    
    def run(self):
        self.window.mainloop()

def main():
    game = ModernTicTacToe()
    game.run()

if __name__ == "__main__":
    main()