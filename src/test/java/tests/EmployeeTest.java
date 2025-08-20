package tests;

import io.github.bonigarcia.wdm.WebDriverManager;

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.*;
import Pages.Login_page;
import Pages.DashboardPage;
import Pages.PimPage;

public class EmployeeTest {
    WebDriver driver;
    Login_page login;
    DashboardPage dashboard;
    PimPage pim;

    @BeforeMethod
    public void setup() {
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");
        driver.manage().window().maximize();
        login = new Login_page(driver);
        dashboard = new DashboardPage(driver);
        pim = new PimPage(driver);

        login.enterUsername("Admin");
        login.enterPassword("admin123");
        login.clickLogin();
    }

    @Test
    public void testAddAndVerifyEmployees() {
        dashboard.goToPIM();
        String[][] employees = {{"John","Doe"}, {"Jane","Smith"}, {"David","Brown"}};

        // 1. Add employees
        for (String[] emp : employees) {
            pim.addEmployee(emp[0], emp[1]);

            // wait for save to complete (redirect to Personal Details page)
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.xpath("//h6[text()='Personal Details']")
            ));

            // Navigate back to PIM -> Add Employee for next iteration
            dashboard.goToPIM();
        }

        // 2. Verify employees
        for (String[] emp : employees) {
            String firstName = emp[0];
            String lastName = emp[1];

            pim.searchEmployee(firstName);   // 🔎 Search only by first name

            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            WebElement result = wait.until(ExpectedConditions.visibilityOfElementLocated(
                By.xpath("//div[@role='row']//div[normalize-space()='" + firstName + "']")
            ));

            // ✅ Assert that the cell text matches the first name
            Assert.assertEquals(result.getText().trim(), firstName, firstName + " not found!");

            System.out.println(firstName + " Verified");
        }
    }

    @AfterMethod
    public void tearDown() {
        dashboard.logout();
        driver.quit();
    }
}
