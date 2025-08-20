package tests;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.*;
import Pages.Login_page;
import Pages.DashboardPage;

public class LoginTest {
    WebDriver driver;
    Login_page login;
    DashboardPage dashboard;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        driver.manage().window().maximize();
        login = new Login_page(driver);
        dashboard = new DashboardPage(driver);
    }

    @Test
    public void testValidLogin() {
        login.enterUsername("Admin");
        login.enterPassword("admin123");
        login.clickLogin();
        
        Assert.assertTrue(driver.getCurrentUrl().contains("dashboard"));
        dashboard.logout();
    }

    @AfterMethod
    public void tearDown() {
        driver.quit();
    }
}
